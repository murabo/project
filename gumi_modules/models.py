# coding: utf-8

from datetime import timedelta
from eventmodules.application.gate import constants as ESV
from eventmodules.components.comp_event_place.models import EventPlace, \
    EventPlaceYakuza, EventPlaceTreasure, EventPlacePays
from eventmodules.components.comp_gate.models import PlayerStockItem
from eventmodules.components.comp_raid.models import RaidBattle
from gredis.attribute import AttributeRedis
from module.wrapper.entity import get_entity
from module.wrapper.gift import gift_official_presents
from yakuza.models import Yakuza
import datetime
import random



class PlayerPlace(AttributeRedis):

    attributes = {
        'is_entry': 0,                         # イベ参加フラグ
        'last_place_id': 0,                    # 前回進んだエリア
        'next_place_id': 872,                  # 今回進むエリア
        'achievement': 0,                      # 現在のエリアの進度
        'is_boss_clear': 0,                    # ボスを倒したか(イベント個別でボス出る場所設定)
        'last_sort': 0,                        # エリアボスバトルでの最後のソート順
        'place_grade': 1,                      # エリアのグレード
        'place_raid': 0,                       # ボスが出現中の時にIDが入る
        '_place_limit_time': 0,                # 追跡中エリアの終了時刻
        'is_entry_place': 0,                   # 追跡エリアに突入したかどうか
        'is_entry_bossarea': 0,                # ボスエリアに突入したかどうか
        'stock_chicket_count': 0,              # ガチャチケのストック数
        'stock_yakuza_count_normal_plus': 0,   # 舎弟(N+)のストック数
        'stock_yakuza_count_rare': 0,          # 舎弟(R)のストック数
        'stock_yakuza_count_rare_plus': 0,     # 舎弟(R+)のストック数
        'stock_money_count': 0,                # 銭のストック数
        'stock_medal_count': 0,                # レア代紋のストック数
        'is_all_clear':0,                      # イベント完全制覇したかどうか
        'total_defeat_boss_count':0,           # ボスを総計何体倒したか
        'has_suicide_count':0,                 # 特攻を何体所持しているか
        'suicide_up_point_rate':1,             # イベントポイントを何倍獲得できるか（特攻ポイント負荷軽減用フィールド）
    }

    def __init__(self, event, player):
        super(PlayerPlace, self).__init__(player=player, event=event)
        self.player = player
        self.event = event

    def get_kvs_key(self, **kwargs):
        player = kwargs.get('player', None)
        event = kwargs.get('event', None)
        return 'Event:%s:%s:%s' % (event.module, event.id, player.pk)
    
    @property
    def place_limit_time(self):
        _place_limit_time = self._place_limit_time
        if not _place_limit_time:
            dt = 0
        else:
            dt = datetime.datetime.strptime(_place_limit_time, '%Y/%m/%d %H:%M:%S')
        return dt
    
    def is_place_timeout(self):
        timeout = False
        if not self.place_limit_time:
            timeout = True
        elif self.place_limit_time < datetime.datetime.now():
            timeout = True
        return timeout
    
    def add_place_time(self, time=0):
        #エリア時間の延長
        place_limit_time = self.place_limit_time + timedelta(minutes=time)
        self.set_time(place_limit_time)
        
        #ボスの時間延長
        raidbattle = RaidBattle.get(self.place_raid)
        raidbattle.close_at = place_limit_time
        
        raidbattle.save()
        self.save()
    
    def get_place_remaining_time(self):
        remaining_time = 0
        if not self.place_limit_time:
            return 0
        if self.place_limit_time > datetime.datetime.now():
            remaining_time = self.place_limit_time - datetime.datetime.now()
            remaining_time = "%d:%02d:%02d" % (remaining_time.seconds / 3600, remaining_time.seconds % 3600 / 60, remaining_time.seconds % 60)
        
        return remaining_time
    
    def set_place_time(self):
        limit_time = ESV.PLACE_LIMIT_TIME[self.place_grade]
        place_limit_time = datetime.datetime.now() + timedelta(minutes=limit_time)
        self.set_time(place_limit_time)
        self.save()

    def set_time(self, dt):
        self._place_limit_time = dt.strftime('%Y/%m/%d %H:%M:%S')

    def update_place_grade(self):
        if not self.place_grade:
            self.place_grade = 1
        else:
            self.place_grade += 1
            self.total_defeat_boss_count += 1

        max_place_grade = max(ESV.MAX_PLACE_ID_FOR_PLACE_GRADE.keys())

        if self.place_grade > max_place_grade:
            self.is_all_clear = 1
            self.place_grade = max_place_grade
            
        self.save()
    
    def area_start(self, player):
        self.reset_stock_item(player)
        self.set_place_time()
        self.is_entry_place = 1
        self.save()
    
    def reset_place(self, reset_flg=0):
        self.last_place_id = ESV.MIN_PLACE_ID - 1
        self.next_place_id = ESV.MIN_PLACE_ID
        self.achievement = 0
        self.reset_stock_count()
        
        if reset_flg == ESV.PLACE_RESET_TIMEOUT:
            self._place_limit_time = 0
            self.is_entry_place = 0
            self.is_entry_bossarea = 0
        
        elif reset_flg == ESV.PLACE_RESET_UPGRADE:
            self._place_limit_time = 0
            self.is_entry_place = 0
            self.is_entry_bossarea = 0
            self.update_place_grade()
       
        self.save()

    def reset_stock_count(self, reset_flg=0):
        self.stock_chicket_count = 0
        self.stock_yakuza_count_normal_plus = 0
        self.stock_yakuza_count_rare = 0
        self.stock_yakuza_count_rare_plus = 0
        self.stock_medal_count = 0
        self.stock_money_count = 0
        self.save()

    def is_boss(self):
        # ボスと遭遇するエリアか
        event_place = EventPlace.get(self.next_place_id)
        is_boss = None
        if event_place.is_boss:
            mygrade_boss_area = ESV.MAX_PLACE_ID_FOR_PLACE_GRADE[self.place_grade]
            is_boss = 1 if mygrade_boss_area == self.next_place_id else 0
        return is_boss

    def get_consume_power(self):
        # 消費体力取得
        return EventPlace.get(self.next_place_id).consume_power

    def get_add_exp(self):
        # 追加経験値
        return EventPlace.get(self.next_place_id).exp

    def get_place_card(self):
        next_place_id = self.next_place_id
        place_cards = EventPlaceYakuza.get_place_yakuza(ESV.EVENT_ID)

        card_ids = []
        for place_card in place_cards:
            min_place, max_place = place_card.min_place, place_card.max_place
            if not min_place or not max_place:
                continue

            if min_place <= next_place_id <= max_place:
                card_ids.append(place_card.yakuza_id)

        if not card_ids:
            raise ValueError(
                ESV.EVENT_RAISE_MESSAGES.get(ESV.EVENT_RAISE_MESSAGE_REWARD) % self.get_place_name()
            )
        
        yakuza_id = random.choice(card_ids)
        yakuza = Yakuza.get(yakuza_id)
        return yakuza
    
    def get_place_treasure(self, player_category):
        next_place_id = self.next_place_id
        place_treasures = EventPlaceTreasure.get_place_treasure(ESV.EVENT_ID)

        treasure_ids = []
        for place_treasure in place_treasures:
            min_place = place_treasure.min_place
            max_place = place_treasure.max_place
            if not min_place or not max_place:
                continue

            if min_place <= next_place_id <= max_place:
                if [0, player_category] in place_treasure.limited_category:
                    treasure_ids.append(place_treasure.treasure_id)

        if not treasure_ids:
            raise ValueError(
                ESV.EVENT_RAISE_MESSAGES.get(ESV.EVENT_RAISE_MESSAGE_REWARD) % self.get_place_name()
            )

        return random.choice(treasure_ids)

    def get_getting_money(self):
        # 追加される銭の最小と最大値
        event_place = EventPlace.get(self.next_place_id)
        return random.randint(event_place.min_money, event_place.max_money)

    def get_pay_category(self):
        next_place_id = self.next_place_id

        place_pays = EventPlacePays.get_place_pay(ESV.EVENT_ID)

        pays = []
        for place_pay in place_pays:
            min_place, max_place = place_pay.min_place, place_pay.max_place
            if not min_place or not max_place:
                continue

            if min_place <= next_place_id <= max_place:
                pays.append(
                    (
                        place_pay.probability_group.category,
                        place_pay.probability_group.probability
                    )
                )

        if not pays:
            raise ValueError(
                ESV.EVENT_RAISE_MESSAGES.get(ESV.EVENT_RAISE_MESSAGE_REWARD) % self.get_place_name()
            )

        category = self.choice_at_random(pays, 100)

        return category if category else ESV.EVENT_PAY_NONE

    def choice_at_random(self, values, max_probability):
        probability = random.randint(1, max_probability)
        accumulate_probability = 0
        for value, _probability in values:
            accumulate_probability += _probability
            if probability <= accumulate_probability:
                return value
        return None

    def get_place_multiple(self):
        # 進行度倍率
        event_place = EventPlace.get(self.next_place_id)
        multiple_procs = [
            [4, event_place.multiple_4],
            [3, event_place.multiple_3],
            [2, event_place.multiple_2]
        ]

        multiple = self.choice_at_random(multiple_procs, 10000)

        return multiple if multiple else 1

    def get_place_progress(self):
        # 進行度
        event_place = EventPlace.get(self.next_place_id)
        return random.randint(event_place.min_achievement, event_place.max_achievement)

    def get_place_text(self):
        # 地回り中テキスト
        event_place = EventPlace.get(self.next_place_id)
        return event_place.detail_text
 
    def get_place_name(self):
        # エリア名テキスト
        event_place = EventPlace.get(self.next_place_id)
        if event_place:
            return event_place.name
        return None

    def get_event_point(self):
        return random.randint(ESV.EVENT_WALK_POINT[0], ESV.EVENT_WALK_POINT[1])
    
    def set_suicide_count_and_pointrate(self, has_suicide_count, suicide_up_point_rate):
        """
        所持特攻舎弟数と、特攻ポイント倍率をセットする
        """
        self.has_suicide_count = has_suicide_count
        self.suicide_up_point_rate = suicide_up_point_rate
        self.save()
    
    def is_stock(self):
        """
        現在ストックしているアイテムがあるかどうかを返す
        """
        is_stock = False
        if self.stock_total_count():
            is_stock = True
    
        return is_stock
    
    def stock_total_count(self):
        """
        現在ストックしているアイテムの総数を返す
        """
        stock_total_count = self.stock_chicket_count + \
                            self.stock_yakuza_count_normal_plus + \
                            self.stock_yakuza_count_rare + \
                            self.stock_yakuza_count_rare_plus + \
                            self.stock_medal_count + \
                            self.stock_money_count
            
        return stock_total_count
    
    def set_stock_item(self, player, item_type, item_id, quantity):
        """
        'type-id-quantity'の書式で、String型でデータをredisへ格納
        """
        stock_item_obj = PlayerStockItem(player.pk, ESV.EVENT_ID) 
        string_obj = str(item_type) + '-' + str(item_id) + '-' + str(quantity)
        stock_item_obj.set(string_obj)

    def reset_stock_item(self, player):
        """
        redisへ格納していたストックアイテムを全てデリート
        """
        stock_item_obj = PlayerStockItem(player.pk, ESV.EVENT_ID) 
        stock_item_obj.delete()
    
    def get_stock_item(self, player):
        """
        'type-id-quantity'の書式で格納されているデータを取得し、
        [type, id, quantity]の形式を１要素とする、リストを返却。
        """
        stock_item_obj = PlayerStockItem(player.pk, ESV.EVENT_ID) 
        stock_item = stock_item_obj.get()

        stock_item_list = []
        for reward in stock_item:
            reward_string = reward.split('-')
            reward_int = map(int, reward_string)
            stock_item_list.append(reward_int)
        
        return stock_item_list

    def stock_item_present_bulkinsert(self, player):
        """
        ストックしていたアイテムを、対象のプレイヤーに付与する
        bulkinsertを使って付与する
        """
        stock_item_list = self.get_stock_item(player)
        
        if len(stock_item_list) > 0:
            d = {}
            for type, id, quantity in stock_item_list:
                if (type, id) in d:
                    d[(type, id)] += quantity
                else:
                    d[(type, id)] = quantity
            
            entities = []
            for k, v in d.items():
                type, id = k
                e = get_entity(type, id, v)
                entities.append((e, v, ESV.STOCK_ITEM_PRESENT_COMMENT))

            gift_official_presents(player, entities)
