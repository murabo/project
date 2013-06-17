# -*- coding: utf-8 -*-

"""
ActionLogからノンアクティブなーユーザーのリストを作成します。
"""

from django.core.cache import cache
from django.core.management.base import BaseCommand
from gokudo.player.models import Player
from optparse import make_option
import commands
import random
import datetime
import logging

class Const(object):
    NEED_COUNT = 1000               # 何人分取得してくるか
    UNIT_NUM   = 100                # 分割したリスト一つ分の中に入るIDの数（オプションにしてもいいかも）
    SET_LIMITS = 10                 # 分割数の最大値（オプションにしてもいいかも）
    DELIMITER  = ","                # デリミタ
    
class PlayerListManager(Player):
    
    @classmethod
    def get_player_ids_by_last_login(cls, from_date, to_date, exclude_player_pk_list=[], limit=5):
        '''
        最終ログイン日で制限したプレイヤーのリスト
        @param from_date: {datetime.datetime}
        @param to_date: {datetime.datetime}
        @param exclude_player_pk_list: {list<int>}
        @param limit: {int}
        ''' 
        #player_list = cls.objects.filter(last_login_at__range=(from_date, to_date), level=level).using('replica').exclude(pk__in=exclude_player_pk_list)[offset:limit + offset]
        count = Player.objects.filter(last_login_at__range=(from_date, to_date)).using('replica').exclude(pk__in=exclude_player_pk_list).count()
        offset = 0 if count < limit else random.randint(1, (count - limit))
        player_list = Player.objects.filter(last_login_at__range=(from_date, to_date)).using('replica').exclude(pk__in=exclude_player_pk_list)[offset:limit + offset]
        player_ids = [] if not player_list else [player.pk for player in player_list]
        return player_ids
 
    @classmethod
    def get_player_ids_by_last_login_on_target_range(cls, day, exclude_player_pk_list=[], limit=5, exited=3):
        '''
        過去の指定日から制限日前までで各日付が最終ログイン日のプレイヤーのリスト
        @param day: {int}
        @param exclude_player_pk_list: {list<int>}
        @param limit: {int}
        ''' 
        base = datetime.datetime.now()
        date_list = [base - datetime.timedelta(days=x+1) for x in range(exited, day)]
        player_ids_dict = {}
        for index, date in enumerate(date_list):
            to_date = date + datetime.timedelta(days=1)
            key = str(index + 3)
            player_ids_dict[key] = PlayerListManager.get_player_ids_by_last_login(date, to_date, exclude_player_pk_list, limit)
        return player_ids_dict

    @classmethod
    def set_cached_left_user_by_day_ago(cls, player_ids, day=1, suffix=1, time=5400):
        '''指定日離脱ユーザーリストをキャッシュに入れる'''
        Player.set_cached_left_user_by_day_ago(player_ids, day=day, suffix=suffix, time=time)
        return None
    
    @classmethod
    def get_cached_left_user_by_day_ago(cls, day=1, suffix=1, limit=0):
        '''指定日離脱ユーザーリストをキャッシュから取得する'''
        return Player.get_cached_left_user_by_day_ago(day=day, suffix=suffix, limit=limit)
   
    @classmethod
    def set_cached_left_user(cls, player_ids, suffix=1, time=5400):
        '''離脱ユーザーリストをキャッシュに入れる'''
        Player.set_cached_left_user(player_ids, suffix=suffix, time=time)
        return None
    
    @classmethod
    def get_cached_left_user(cls, suffix=1, limit=0):
        '''離脱ユーザーリストをキャッシュから取得する'''
        return Player.get_cached_left_user(suffix=suffix, limit=limit)

class Util(object):
    
    @staticmethod
    def change_csv_str_to_list(csv_str, delimiter=Const.DELIMITER, val_type=None):
        '''
        カンマ区切りの文字列をリストに変換
        @param csv_str: {str} 変換したい"1,2,3"形式の文字列
        @param delimiter: {str} 区切り文字
        @param val_type: {Object} or {str} 返還後のリスト内の型（None,str,int以外非推奨）
        @return: {list}
        '''
        str_list = csv_str.split(delimiter)
        if val_type is None or val_type == str or val_type == "str":
            changed_list = [val for val in str_list if val]
        elif val_type == int or val_type == "int":
            changed_list = [int(val) for val in str_list if val]
        else: # 非推奨
            type_str = str(val_type)
            type_str = type_str.strip("<type '")
            type_str = type_str.strip("'>")
            changed_list = [eval("".join((type_str, "(", val, ")"))) for val in str_list]
        return changed_list
    
    @staticmethod
    def change_list_to_str(use_list, delimiter=Const.DELIMITER):
        '''
        リストをカンマ区切りのテキストに変換
        @param use_list: {list} 変換したいリスト
        @param delimiter: {str}
        @return: {list}
        '''
        text = delimiter.join(map(str, use_list))
        return text
    
    @staticmethod
    def split_list(target_list, unit_num=Const.UNIT_NUM, set_limits=Const.SET_LIMITS):
        '''
        大きなリストを分割して「リストのリスト」を返す
        @param target_list: {list}
        @param unit_num: {int} 分割した単位リストの内包数
        @param set_limits: {int} 分割する個数（の最大値）
        '''
        if len(target_list) < unit_num:
            return [target_list]
        lists = []
        for i in range(set_limits):
            if len(target_list) >= unit_num:
                temp_list = target_list[0:unit_num]
                del target_list[0:unit_num]
                lists.append(temp_list)
        return lists
 
class Command(BaseCommand):

    help = u'''ActionLogからノンアクティブなユーザーのリストを作成します。'''
    option_list = BaseCommand.option_list + (
        make_option('--show',
            action='store_true',
            dest='show',
            default=False,
            help=u'show made lists'),
    )
    MONTH = 30 

    def handle(self, *args, **options):
        '''
        main
        '''
        is_show_mode = options.get('show', False)
        logging.debug('start...')
        
#        # ① 最終ログイン日毎のユーザ TODO:使ってるメソッドが確認とれ次第運用開始
#        each_last_login_ids = PlayerListManager.get_player_ids_by_last_login_on_target_range(self.MONTH)
#        for index, day in enumerate(range(3, self.MONTH)):
#            dic_index = str(day)
#            player_ids = each_last_login_ids[dic_index]
#            logging.debug(dic_index + ' days ago: ' + str(len(player_ids)) + ' ppl')
#            player_ids_nest = Util.split_list(player_ids, Const.UNIT_NUM, Const.SET_LIMITS)
#            for nest_index, ids in enumerate(player_ids_nest):
#                PlayerListManager.set_cached_left_user_by_day_ago(ids, day=day, suffix=nest_index + 1, time=5400)
#
        # ② 最終ログイン日が7日前から3日前のユーザー
        logging.debug('7 - 3 days')
        limit = Const.NEED_COUNT
        from_date = datetime.datetime.now() - datetime.timedelta(days=8)
        to_date = datetime.datetime.now() - datetime.timedelta(days=3)
        player_ids = PlayerListManager.get_player_ids_by_last_login(from_date, to_date, limit=limit)
        logging.debug('   ' + str(len(player_ids)) + 'ppl')

        
        # ③ 最終ログイン日が30日前から8日前のユーザー
        if len(player_ids) != Const.NEED_COUNT:
            logging.debug('30 - 8 days')
            limit = Const.NEED_COUNT - len(player_ids)
            from_date = datetime.datetime.now() - datetime.timedelta(days=31)
            to_date = datetime.datetime.now() - datetime.timedelta(days=8)
            player_ids2 = PlayerListManager.get_player_ids_by_last_login(from_date, to_date, limit=limit)
            logging.debug('   ' + str(len(player_ids2)) + 'ppl')
            player_ids.extend(player_ids2)
        
        random.shuffle(player_ids)
        player_id_lists = Util.split_list(player_ids, Const.UNIT_NUM, Const.SET_LIMITS)
        
        i = 0
        for l in player_id_lists:
            i = i + 1
            list_str = Util.change_list_to_str(l)
            PlayerListManager.set_cached_left_user(list_str, i)
        logging.debug('Cached')
        
        if is_show_mode:
            for j in range(i):
                logging.debug('List %s :' % [j + 1, PlayerListManager.get_cached_left_user(j + 1)])
                
        logging.debug('finish')



