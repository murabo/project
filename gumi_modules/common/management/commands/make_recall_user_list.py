# -*- coding: utf-8 -*-

"""
最終ログイン日から、呼び戻し対象ユーザーのリストを作成します。
"""

from django.core.management.base import BaseCommand
from gokudo.player.models import Player
from optparse import make_option
from common.datetime_util import DatetimeUtil
from glot import init as glot_init, get as glot_get
import datetime

class RecallPlayerListManager(Player):
    '''
    呼び戻し関連
    '''
    @classmethod
    def get_player_ids_by_last_login(cls, from_date, exclude_player_pk_list=[]):
        '''
        最終ログイン日で制限したプレイヤーのリスト
        @param from_date: {datetime.datetime}
        @param exclude_player_pk_list: {list<int>}
        ''' 
        player_list = Player.objects.filter(last_login_at__lte=from_date).using('replica').exclude(pk__in=exclude_player_pk_list)[:10000]
        player_ids = [] if not player_list else [player.pk for player in player_list]
        return player_ids
 
    @classmethod
    def set_recall_user(cls, player_ids):
        '''離脱ユーザーリストをglotに入れる'''
        dt = DatetimeUtil.now()
        shard = 1
        if dt.hour % 2 > 0:
            shard = 2
        result = glot_init('recall_user', [(player_id, 1) for player_id in player_ids], shard=shard)
        print "\x1b[1;40m\x1b[1;32m Done \x1b[0m" if result else "\x1b[1;42m\x1b[1;37m Canceled \x1b[0m"
        return result
      
class Command(BaseCommand):

    help = u'''最終ログイン日から呼び戻し対象ユーザーのリストを作成します。'''
    option_list = BaseCommand.option_list + (
        make_option('--show',
            action='store',
            dest='show',
            type='int',
            default=0,
            help=u'show made lists'),
    )
    def handle(self, *args, **options):
        '''
        main
        '''
        is_show_mode = options.get('show', 0)
        # 最終ログイン日が14日以上前のユーザー
        from_date = DatetimeUtil.now() - datetime.timedelta(days=14)
        player_ids = RecallPlayerListManager.get_player_ids_by_last_login(from_date)
        print ''.join([str(len(player_ids)) + 'ppl'])
        result = RecallPlayerListManager.set_recall_user(player_ids)
        if result and is_show_mode > 0:
            print_count = 0
            while print_count < is_show_mode:
                print ':'.join([str(print_count), glot_get('recall_user')])
                print_count += 1
            print '\x1b[1;40m\x1b[1;32m ex-dump exit \x1b[0m'

