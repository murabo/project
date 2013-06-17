# -*- coding: utf-8 -*-

"""
スカイヤクザツリー第２回目の秘宝補填しきれていない件の対応

対象は地回りで必ずもらえるはずの秘宝。
補填対象者は、第２回目をプレイしている人、すなわちスカイヤクザツリー専用TTにデータがある人全員。
ただし、TTから対象者を探すのは実質無理があるので、ログから探す。
"""

import datetime
import sys
import threading
import time
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from player.models import Player
from gokujo.models import Gokujo,PlayerGokujo,PlayerTreasureCategory
from eventmodule.e134_yakuzatree import constants as ESV
from eventmodule.e134_yakuzatree.utils.base_utils import get_event_player_place, get_place_treasure

from common.static_values import StaticValues
from common.inspector_utils import InspectorLogUtils

MAX_SEND_COUNT=20

if settings.OPENSOCIAL_DEBUG:
    MAX_SEND_COUNT=2

def logging_method(message, print_flg=True):
    if not print_flg:
        return
    message = "%s" % (message)
    try:
        sys.stdout.write('%s\n' % message.encode('utf-8','ignore'))
        sys.stdout.flush()
    except:
        print message

def presenter(osuser_ids, is_debug=True):
    """
    リストで渡ってきたosuserに秘宝を補填する
    """
    def get_treasures(player, place_id):
        "取得可能なはずの秘宝リスト"
        ret = []
        place_treasure_category = ESV.EVENT_PLACE_TREASURES.keys()
        for can_get_place_id in place_treasure_category:
            if can_get_place_id <= place_id:
                gokujo = get_place_treasure(player, can_get_place_id)
                if not gokujo:
                    return None
                ret.append(gokujo)
        return ret

    def set_treasures(player, gokujos, is_debug):
        if not gokujos:
            return

        for gokujo in gokujos:
            inscpector_logs = []
            player_gokujo = PlayerGokujo.get_cache_by_player_gokujo(player, gokujo)
            if player_gokujo and player_gokujo.check_treasure_is_encount():
                continue

            logging_method(u'is_debug %s player %s gokujo %s category %s' % (is_debug, player.pk, gokujo.pk, player_gokujo.treasure_category))
            if is_debug:
                continue
            PlayerTreasureCategory.assign(player, gokujo)
            gokujo_list=Gokujo.get_list_by_treasure_category(gokujo.treasure_category)
            for gj in gokujo_list:
                PlayerGokujo.assign_treasure(player, gj)
                inscpector_logs.append((StaticValues.TYPE_TREASURE, gj.pk, 0, 1))
            PlayerGokujo.check_complete_by_treasure(player, gokujo.treasure_category)
            PlayerTreasureCategory.set_is_complete(player, gokujo.treasure_category)
            InspectorLogUtils.write_create_log(player, inscpector_logs, InspectorLogUtils.REASON_REPAIR)
    
    for ouserid in osuser_ids:
        player = Player.get(ouserid)
        try:
            event_player_place = get_event_player_place(player)
            gokujos = get_treasures(player, event_player_place.last_place_id)
            set_treasures(player, gokujos, is_debug)
        except:
            pass #ouserid is none player

class PresentSender(threading.Thread):
    """
    別スレッドで送付してみる
    """
    def set_data(self, osuser_ids, is_debug=True):
        self.osuser_ids = osuser_ids
        self.is_debug = is_debug
    
    def run(self):
        try:
            ThreadPoolCounter.increase()
            presenter(self.osuser_ids, self.is_debug)
        finally:
            #例外関係なく、カウンター処理は必要
            ThreadPoolCounter.decrease()


class ThreadPoolCounter(object):
    """
    スレッドプール風の動作をさせるためのカウンタ
    """
    thread_pool_counter = 0
    THREAD_POOL_CAPACITY = 10
    #THREAD_POOL_CAPACITY = 2
    lock = threading.Lock() #thread_pool_counter用ロック
    
    @classmethod
    def wait(cls):
        while 1:
            if cls.thread_pool_counter >= cls.THREAD_POOL_CAPACITY:
                time.sleep(0.5)
            else:
                break
    
    @classmethod
    def wait_for_zero(cls):
        while 1:
            if cls.thread_pool_counter > 0:
                time.sleep(0.5)
            else:
                break
    
    @classmethod
    def increase(cls, number=1):
        cls.lock.acquire(0)
        cls.thread_pool_counter += 1
        cls.lock.release()
    
    @classmethod
    def decrease(cls, number=1):
        cls.lock.acquire(0)
        cls.thread_pool_counter -= 1
        cls.lock.release()


def compensate_treasure(filename, is_debug=True):
    """
    osuserを全員分ループし、プレゼントしていく

    filenameは1行osuseridだけのリスト
    """
    def do_thread(osuser_ids):
        all_count = len(ouser_ids)
        logging_method(u'[%s] start. all_count=%s ' % (datetime.datetime.now().strftime("%H:%M:%S"),  all_count))

        ThreadPoolCounter.wait()
        present_sender = PresentSender()
        present_sender.set_data(ouser_ids, is_debug)
        present_sender.start()

    ouser_ids = []
    max_num = 1000
    f=open(filename)
    for line in f:
        ouser_ids.append(int(line))
        if len(ouser_ids) < max_num:
            continue

        do_thread(ouser_ids)
        ouser_ids = []

    if len(ouser_ids):
        do_thread(ouser_ids) #max_numのあまり分を処理
    ThreadPoolCounter.wait_for_zero()

class Command(BaseCommand):

    help = u'''秘宝補填開始します'''

    option_list = BaseCommand.option_list + (
        make_option('--exec',
            action='store_true',
            dest='execute',
            default=False,
            help=u'実際に補填します'),
    )

    def handle(self, *args, **options):
        start_time = datetime.datetime.today()
        time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
        logging_method(u'%s 秘宝補填開始します\n' % (time_str))

        is_debug = False
        if not options.get('execute', False):
            is_debug = True
            logging_method(u'デバッグモードです')

        #osuser_idのリスト。対象者はログから探す。
        filename = args[0]
        compensate_treasure(filename, is_debug)

        logging_method('')
        end_time = datetime.datetime.today()
        time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")
        if is_debug:
            logging_method(u'デバッグモードです')

        time_str = str(end_time-start_time)
        logging_method(u'実行時間:%s' % (time_str))
