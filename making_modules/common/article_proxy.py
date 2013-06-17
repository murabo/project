# -*- coding:utf-8 -*-
from common.static_values import StaticValues

from present.models import PlayerPresent
from item.models import GameItem, PlayerItem
from yakuza.models import Yakuza, PlayerYakuza
from gokujo.models import Gokujo, PlayerGokujo
from equipment.models import GokujoEquipmentItem, YakuzaEquipmentItem, PlayerGokujoEquipmentItem, PlayerYakuzaEquipmentItem
from point.constants import PointStatic

'''
舎弟、アイテム等のラッパークラス
Proxyパターンそのものなので、Proxyで。

目的はStaticValuesに依存している、書き方をできる限りなくすこと。
ほぼ同じような似た処理をところどころに分散して毎回書いているのでこれらを統一化したい。

問題:type,idなどPythonの関数を変数名として使用せざるを得ない。

テスト:common/article_proxy.pyがテスト
'''

class BaseArticleProxy(object):
    '''
    Baseクラス
    基本的な処理はこちらに追加すること
    '''
    @classmethod
    def is_none(cls, type):
        return type == StaticValues.TYPE_NONE

    @classmethod
    def is_card(cls, type):
        return type == StaticValues.TYPE_CARD

    @classmethod
    def is_item(cls, type):
        return type == StaticValues.TYPE_ITEM

    @classmethod
    def is_treasure(cls, type):
        return type == StaticValues.TYPE_TREASURE

    @classmethod
    def is_money(cls, type):
        return type == StaticValues.TYPE_MONEY

    @classmethod
    def is_point(cls, type):
        return type == StaticValues.TYPE_POINT

    @classmethod
    def is_medal(cls, type):
        return type == StaticValues.TYPE_MEDAL

    @classmethod
    def is_loginbonus(cls, type):
        return type == StaticValues.TYPE_LOGINBONUS

    @classmethod
    def is_num(cls, type):
        '''
        オブジェクトでは無く、数値で管理しているもの
        銭、盃PT、レアメダル
        '''
        return cls.is_money(type) or cls.is_point(type) or cls.is_medal(type)

    @classmethod
    def is_gokujoequip(cls, type):
        return type == StaticValues.TYPE_GOKUJOEQUIP

    @classmethod
    def is_yakuzaequip(cls, type):
        return type == StaticValues.TYPE_YAKUZAEQUIP

    @classmethod
    def is_equip(cls, type):
        '''
        装備品か?
        '''
        return cls.is_gokujoequip(type) or cls.is_yakuzaequip(type)

    @classmethod
    def is_article(cls, type):
        if cls.is_none(type):
            return False
        if cls.is_num(type):
            return False
        return True

    @classmethod
    def get_class(cls, type):
        '''
        typeに対応するクラスを返す
        クラスがない場合はNoneを返す
        '''
        obj = None
        if cls.is_none(type):
            pass
        elif cls.is_num(type):
            #TODO:is_numの場合どうする?
            #とりあえず、Noneで
            pass
        elif cls.is_card(type):
            obj = Yakuza
        elif cls.is_item(type):
            obj = GameItem
        elif cls.is_treasure(type):
            obj =Gokujo
        elif cls.is_gokujoequip(type):
            obj = GokujoEquipmentItem
        elif cls.is_yakuzaequip(type):
            obj = YakuzaEquipmentItem
        return obj

    @classmethod
    def get_player_class(cls, type):
        '''
        get_classのプリエヤークラス版
        '''
        obj = None
        if cls.is_none(type) or cls.is_num(type):
            pass
        elif cls.is_card(type):
            obj = PlayerYakuza
        elif cls.is_item(type):
            obj = PlayerItem
        elif cls.is_treasure(type):
            obj = PlayerGokujo
            if not obj.is_treasure:
                obj = None
        elif cls.is_gokujoequip(type):
            obj = PlayerGokujoEquipmentItem
        elif cls.is_yakuzaequip(type):
            obj = PlayerYakuzaEquipmentItem
        return obj

    @classmethod
    def get_object(cls, type, id, num=1):
        '''
        typeに対応するオブジェクトを返す
        '''
        obj = None
        if cls.is_none(type):
            pass
        elif cls.is_num(type):
            obj = int(num)
        else:
            kls = cls.get_class(type)
            obj = kls.get(id)
        return obj

    @classmethod
    def get_object_type_id(cls, obj):
        '''
        インスタンスからtype,idを取得する
        銭などはint/longなので判定できない。どうするか?
        あれば便利だが実質現在のコードでは使っていないので、後回し?

        ひとまず作成したが、テストは書いていない。様子見
        '''
        if obj is None:
            return {'type':StaticValues.TYPE_NONE, 'id':None}
        elif isinstance(obj, Yakuza):
            return {'type':StaticValues.TYPE_CARD, 'id':int(obj.pk)}
        elif isinstance(obj, PlayerYakuza):
            return {'type':StaticValues.TYPE_CARD, 'id':int(obj.yakuza.pk)}
        elif isinstance(obj, GameItem):
            return {'type':StaticValues.TYPE_ITEM, 'id':int(obj.pk)}
        elif isinstance(obj, PlayerItem):
            return {'type':StaticValues.TYPE_ITEM, 'id':int(obj.item.pk)}
        elif isinstance(obj, Gokujo):
            return {'type':StaticValues.TYPE_TREASURE, 'id':int(obj.pk)}
        elif isinstance(obj, PlayerGokujo):
            return {'type':StaticValues.TYPE_TREASURE, 'id':int(obj.gokujo.pk)}
        elif isinstance(obj, GokujoEquipmentItem):
            return {'type':StaticValues.TYPE_GOKUJOEQUIP, 'id':int(obj.pk)}
        elif isinstance(obj, PlayerGokujoEquipmentItem):
            return {'type':StaticValues.TYPE_GOKUJOEQUIP, 'id':int(obj.equipment_id)}
        else:
            #TODO:銭などの場合
            return {'type':StaticValues.TYPE_NONE, 'id':None}

    @classmethod
    def image_url(cls, type, id=0):
        if cls.is_none(type):
            "画像は存在しない"
            return None
        elif cls.is_money(type):
            obj = PointStatic('money')
            return obj.image_url()
        if cls.is_point(type):
            obj = PointStatic('point')
            return obj.image_url()
        if cls.is_medal(type):
            obj = PointStatic('medal')
            return obj.image_url()
        else:
            obj = cls.get_object(type, id)
            try:
                return obj.image_url()
            except AttributeError:
                return None

    @classmethod
    def image_url_m(cls, type, id=0):
        url = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
            url = obj.image_url_m()
        elif cls.is_point(type):
            obj = PointStatic('point')
            url = obj.image_url_m()
        elif cls.is_medal(type):
            obj = PointStatic('medal')
            url = obj.image_url_m()
        else:
            obj = cls.get_object(type, id)
            try:
                url = obj.image_url_m()
            except AttributeError:
                pass
        return url

    @classmethod
    def image_url_comp(cls, type, id=0):
        url = None
        if cls.is_none(type) or cls.is_num(type):
            pass
        else:
            obj = cls.get_object(type, id)
            try:
                url = obj.image_url_comp()
            except AttributeError:
                pass
        return url

    @classmethod
    def image_comp_for_media(cls, type, id=0):
        url = None
        if cls.is_none(type) or cls.is_num(type):
            pass
        else:
            obj = cls.get_object(type, id)
            try:
                url = obj.get_image_comp_for_media()
            except AttributeError:
                pass
        return url

    @classmethod
    def image_m_for_media(cls, type, id=0):
        url = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
        elif cls.is_point(type):
            obj = PointStatic('point')
        elif cls.is_medal(type):
            obj = PointStatic('medal')
        else:
            obj = cls.get_object(type, id)
        try:
            img = obj.get_image_m_for_media()
        except AttributeError:
            pass
        return img

    @classmethod
    def image_url_s(cls, type, id=0):
        url = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
            url = obj.image_url_s()
        elif cls.is_point(type):
            obj = PointStatic('point')
            url = obj.image_url_s()
        elif cls.is_medal(type):
            obj = PointStatic('medal')
            url = obj.image_url_s()
        else:
            obj = cls.get_object(type, id)
            try:
                url = obj.image_url_s()
            except AttributeError:
                pass
        return url

    @classmethod
    def image_s_for_media(cls, type, id=0):
        url = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
        elif cls.is_point(type):
            obj = PointStatic('point')
        elif cls.is_medal(type):
            obj = PointStatic('medal')
        else:
            obj = cls.get_object(type, id)
        try:
            img = obj.get_image_s_for_media()
        except AttributeError:
            pass
        return img


    @classmethod
    def image_url_mini(cls, type, id=0):
        url = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
        elif cls.is_point(type):
            obj = PointStatic('point')
        elif cls.is_medal(type):
            obj = PointStatic('medal')
        else:
            obj = cls.get_object(type, id)
            
        try:
            url = obj.image_url_mini()
        except AttributeError:
            pass
        return url


    @classmethod
    def image_mini_for_media(cls, type, id=0):
        img = None
        if cls.is_none(type):
            pass
        elif cls.is_money(type):
            if id == 50000:
                obj = PointStatic('money_50000')
            else:
                obj = PointStatic('money')
        elif cls.is_point(type):
            obj = PointStatic('point')
        elif cls.is_medal(type):
            obj = PointStatic('medal')
        else:
            obj = cls.get_object(type, id)
        try:
            img = obj.get_image_mini_for_media()
        except AttributeError:
            pass
        return img

    @classmethod
    def name(cls, type, id):
        if cls.is_none(type):
            return None
        elif cls.is_money(type):
            return u"%s銭" % id
        elif cls.is_point(type):
            return u"盃%spt" % id
        elif cls.is_medal(type):
            return u"ﾚｱ代紋%s枚" % id
        else:
            obj = cls.get_object(type, id)
            return obj.name
    
    @classmethod    
    def wrapper_name(cls, type, id, num):
        if cls.is_item(type) and num > 1:
            obj = cls.get_object(type, id)
            num = u"%s個" % num
            return obj.name + num
        else:
            return cls.name(type, id)

class ArticleProxy(BaseArticleProxy):
    '''
    BaseArticleProxyを継承したクラス
    外部からはこちらを使うこと

    BaseArticleProxyに入れるのは不適切な処理はこっちに入れる
    '''

    @classmethod
    def give_official_present(cls, player, type, id, txt, num=1, time_limited=None):
        '''
        PlayerPresent.give_official_present()を呼ぶだけ
        '''
        obj = cls.get_object(type, id, num)
        if not obj:
            return None
        if cls.is_treasure(type) and not obj.is_treasure:
            #give_official_present側でチェックしていないのでする
            return None
        return PlayerPresent.give_official_present(player, obj, txt, num=num, type=type, time_limited=time_limited)

    @classmethod
    def assign(cls, player, type, id, num=1):
        '''
        プレゼント欄を介さずに、直接付与する
        '''
        if cls.is_none(type):
            return None
        if cls.is_money(type):
            player.add_money(num)
            return num
        elif cls.is_point(type):
            player.add_current_communication_point(num)
            return num
        elif cls.is_medal(type):
            player.add_medal(num)
            return num

        obj = cls.get_object(type, id)
        if not obj:
            return None

        klass = cls.get_player_class(type)
        if not klass:
            return None

        if cls.is_treasure(type):
            ret = klass.assign_treasure(player, obj, num)
        else:
            ret = klass.assign(player, obj, num)
        return ret
