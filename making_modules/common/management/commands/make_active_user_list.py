# -*- coding: utf-8 -*-

"""
ActionLogからアクティブなーユーザーのリストを作成します。
"""

from django.core.cache import cache
from django.core.management.base import BaseCommand
from gokudo.player.models import Player
from optparse import make_option
import commands
import datetime
import random
import time

class Const(object):
    SEARCH_LENGTH = 50000           # ActionLogから取得してくる数、重複が多いので大きな数字（オプションにしてもいいかも）
    UNIT_NUM = 100                  # 分割したリスト一つ分の中に入るIDの数（オプションにしてもいいかも）
    SET_LIMITS = 10                 # 分割数の最大値（オプションにしてもいいかも）
    DIR = "/volume/logs/syslog/"    # ActionLogのディレクトリ
    DELIMITER = ","                 # デリミタ
    TEST_FILE_NAME = "log.txt"      # ローカルテスト用ActionLogファイル名
    TEST_DIR = "$HOME/tmp/"         # ローカルテスト用ActionLogディレクトリ

class Mod(object):
    
    @staticmethod
    def get_serch_file_name(before_days=0, is_test_mode=False):
        '''
        検索対象ファイル名を返す。今日のものから27日前のものまで可能。
        今日なら action_log.YYYY-mm-dd
        それ以外なら action_log.YYYY-mm-dd.gz
        @param before_daysparam:  {int} 何日前のデータを取得するか
        @return : {str} ファイル名
        '''
        if before_days > 27:
            raise Exception
        if before_days == 0:
            file_name = commands.getoutput("echo `date '+action_log.%Y-%m-%d'`")
        else:
            today = datetime.datetime.today()
            y = today.year
            m = today.month
            d = today.day - before_days
            if d < 1:
                m = m - 1
                if m < 1:
                    m = 12
                if m in [1, 3, 5, 7, 8, 10, 12]:
                    d = 31 + d
                elif m in [4, 6, 9, 11]:
                    d = 30 + d
                else:
                    d = 28 + d
            str_y = str(y)
            str_m = str(m)
            str_d = str(d)
            str_m = "0%s" % str_m if len(str_m) == 1 else str_m
            str_d = "0%s" % str_d if len(str_d) == 1 else str_d
            file_name = "action_log.%s-%s-%s.gz" % (str_y, str_m, str_d)
        
        if is_test_mode:
            return Const.TEST_FILE_NAME
        return file_name
        
    @staticmethod
    def get_file_len(file_name, dir, max_len):
        '''
        @param file_name: {str} 検索ファイル名
        @param dir: {str} ディレクトリ名
        @param max_len: {int} 上限値
        @return: {int} ファイルの行数
        '''
        return int(commands.getoutput("tail -n %s %s%s | wc -l" % (max_len, dir, file_name)).strip())
    
    @staticmethod
    def get_active_user_ids_str(file_name, dir, max_len):
        '''
        @param file_name: {str} 検索ファイル名
        @param dir: {str} ディレクトリ名
        @param max_len: {int} 上限値
        @return: {str} アクティブユーザーリスト => "1,2,3"のようなカンマ区切りテキスト
        '''
        active_user_ids = commands.getoutput("tail -n %s %s%s|awk {'print $7'}|sort|uniq" % (max_len, dir, file_name))
        active_user_ids = active_user_ids.strip("\n")
        active_user_ids = active_user_ids.replace("\n", Const.DELIMITER)
        active_user_ids = active_user_ids.replace("None", "0")
        return active_user_ids
    
    @staticmethod
    def get_active_user_ids_str_by_gzip(file_name, dir, max_len):
        '''
        gzipからアクティブユーザーリストをとって文字列で返す。
        @param file_name: {str} 検索ファイル名
        @param dir: {str} ディレクトリ名
        @param max_len: {int} 上限値
        @return: {str} アクティブユーザーリスト => "1,2,3"のようなカンマ区切りテキスト
        '''
        active_user_ids = commands.getoutput("gzip %s%s -dc | head -n %s" % (dir, file_name, max_len))
        active_user_ids = active_user_ids.strip("\n")
        active_user_ids = active_user_ids.replace("\n", ",")
        return active_user_ids
    
class Util(object):
    
    @staticmethod
    def change_csv_str_to_list(csv_str, delimiter=Const.DELIMITER, val_type=None):
        '''
        カンマ区切りの文字列をリストに変換
        @param csv_str: {str} 変換したい"1,2,3"形式の文字列
        @param delimiter: {str} 区切り文字
        @param val_type: {Object} 返還後のリスト内の型（None,str,int以外非推奨）
        @return: {list}
        '''
        str_list = csv_str.split(delimiter)
        if val_type is None or val_type == str or val_type == "str":
            changed_list = [val for val in str_list if val]
        elif val_type == int or val_type == "int":
            changed_list = [int(val) for val in str_list if val and val.isdigit()]
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
        lists = []
        for i in range(set_limits):
            if len(target_list) >= unit_num:
                temp_list = target_list[0:unit_num]
                del target_list[0:unit_num]
                lists.append(temp_list)
        return lists

class Command(BaseCommand):
    
    help = u'''Make active user list from action log.'''
    option_list = BaseCommand.option_list + (
        make_option('--local',
            action='store_true',
            dest='local',
            default=False,
            help=u'local debug'),
        make_option('--show',
            action='store_true',
            dest='show',
            default=False,
            help=u'show made lists'),
    )
    
    @staticmethod
    def make_get_list_method(before_days):
        '''
        @param before_days: {int} 何日前のデータを取得するか
        @return: {function} 検索用メソッド
        '''
        if before_days == 0:
            def _get_list(file_name, dir, max_len):
                return Mod.get_active_user_ids_str(file_name, dir, max_len)
        else:
            def _get_list(file_name, dir, max_len):
                return Mod.get_active_user_ids_str_by_gzip(file_name, dir, max_len)
        return _get_list
    
    def handle(self, *args, **options):
        '''
        main
        '''
        is_test_mode = options.get('local', False)
        is_show_mode = options.get('show', False)
        if is_test_mode:
            print ''
            print '[ Local debug mode! ]'
            print ''
            dir = Const.TEST_DIR
        else:
            dir = Const.DIR
        print datetime.datetime.today()
        start_time = time.time()
        print 'Try to make active user list from action logs.'
        before_days = 0
        serch_file_name = Mod.get_serch_file_name(before_days, is_test_mode)
        get_active_user_ids_str = self.make_get_list_method(before_days)
        print 'Making from "%s%s"' % (dir, serch_file_name)
        active_user_ids = get_active_user_ids_str(serch_file_name, dir, Const.SEARCH_LENGTH)
        #日付が変わったばかりで検索対象が少なかったら昨日のActionLogも見る
        serch_file_len = Mod.get_file_len(serch_file_name, dir, Const.SEARCH_LENGTH)
        if serch_file_len < Const.SEARCH_LENGTH:
            before_days = 0
            serch_file_name = Mod.get_serch_file_name(before_days, is_test_mode)
            print 'And making from "%s%s"' % (dir, serch_file_name)
            get_active_user_ids_str = self.make_get_list_method(before_days)
            active_user_ids_yesterday = get_active_user_ids_str(serch_file_name, dir, Const.SEARCH_LENGTH - serch_file_len)
            if active_user_ids_yesterday is not None:
                active_user_ids = Const.DELIMITER.join((active_user_ids, active_user_ids_yesterday))
                
        id_list = Util.change_csv_str_to_list(active_user_ids, Const.DELIMITER, val_type=int)
        del id_list[0] # 0が含まれている可能性があるのでリストの１番目を削除
        random.shuffle(id_list)
        lists = Util.split_list(id_list, Const.UNIT_NUM, Const.SET_LIMITS)
        i = 0
        for l in lists:
            i = i + 1
            list_str = Util.change_list_to_str(l)
            Player.set_cached_super_active_player_ids(list_str, i)
#            print '    ... List %s created' % (i)
        print '    ... %s lists made and cached!' % (i)
        if is_show_mode:
            for j in range(i):
                print ''
                print 'List %s : ' % (j + 1)
                print Player.get_cached_super_active_player_ids(j + 1)
            print ''
        print 'Done! (%s sec)' % (time.time() - start_time)
        print '* If you want to use these lists, you should call this method.'
        print '  => "Player.get_super_active_players()" or "Player.get_cached_super_active_player_ids(suffix=1..%s)"' % (i)
