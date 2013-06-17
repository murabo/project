# -*- coding: utf-8 -*-

"""
茂木トレードデータ返却スクリプト

RMTの関係で返却が必要になった。元々はトレードバグ修正時に返却が必要になり作成したスクリプト。
海賊道でも使う予定なので一旦スクリプト化。必要なくなったら削除予定

動作
トレードが完了している物以外をプレゼントで返却する。
"""

import sys
import os
import time
from datetime import timedelta, datetime
import thread
from optparse import make_option
from django.core.management.base import BaseCommand
from django.conf import settings

from player.models import Player
from yakuza.models import Yakuza, PlayerYakuza
from item.models import GameItem
from gokujo.models import Gokujo
from trade.models import PlayerTrade, TradeEntry
from present.models import PlayerPresent
from common.static_values import StaticValues

global_print_flg = False
def logging_method(message, print_flg=None):
    if print_flg is None:
        global global_print_flg
        print_flg = global_print_flg

    if not print_flg:
        return False
    message = "%s" % (message)
    try:
        sys.stdout.write('%s\n' % message.encode('utf-8','ignore'))
        sys.stdout.flush()
    except:
        print message
    return True

def get_object(trade_entry):
    if trade_entry.article_type == StaticValues.TYPE_CARD:
        obj = PlayerYakuza.get(trade_entry.article_key)
    elif trade_entry.article_type == StaticValues.TYPE_ITEM:
        obj = GameItem.get(trade_entry.article_key)
    elif trade_entry.article_type == StaticValues.TYPE_TREASURE:
        obj = Gokujo.get(trade_entry.article_key)
    elif trade_entry.article_type in (StaticValues.TYPE_MONEY, StaticValues.TYPE_POINT, StaticValues.TYPE_MEDAL):
        obj = int(trade_entry.article_value)
    else:
        return None
    return obj

#アイテムを返却する
#本番DBにアクセスする
#is_return=Falseの場合、実際にはプレゼントしない
#is_delete=Falseの場合、実際には削除しない
#teはotherのデータなので取得し直す
#TODO:msgは修正の必要がある
#TODO:補償が必要ならばここで追加で行う
def return_item(trade_entry, message, is_return=False, is_delete=False):
    if not trade_entry:
        return False

    obj = get_object(trade_entry)
    if not obj:
        return False

    if trade_entry.trade_action == StaticValues.TRADE_ACTION_REQUEST:
        player = trade_entry.player_trade.from_player
    elif trade_entry.trade_action == StaticValues.TRADE_ACTION_APPROVE:
        player = trade_entry.player_trade.to_player
    else:
        return False

    ret = None
    if is_return:
        if trade_entry.article_type == StaticValues.TYPE_CARD:
            if obj.player:
                #バグで既に所持者がいたら返却しない
                #舎弟以外は所有者はないはず...
                return "Skip_Card_Having"
            ret = PlayerPresent.give_official_present(player, obj, message, num = trade_entry.article_value)
        if trade_entry.article_type in (StaticValues.TYPE_ITEM, StaticValues.TYPE_TREASURE):
            ret = PlayerPresent.give_official_present(player, obj, message, num = trade_entry.article_value)
        elif trade_entry.article_type in (StaticValues.TYPE_MEDAL, StaticValues.TYPE_MONEY, StaticValues.TYPE_POINT):
            ret = PlayerPresent.give_official_present(player, obj, message, type = trade_entry.article_type)
        if ret and is_delete:
            trade_entry.delete()
    return True if ret else False

def return_items(player_trades, message, sleep=False, is_return=False, is_delete=False):
    "複数のplayer_tradeを返却処理する"
    if not player_trades:
        return

    count = 0
    for player_trade in player_trades:
        outstr = u'[IsReturn] %s [IsDelete] %s [PlayerTradeID] %s [FromPlayerID] %s [ToPlaeyrID] %s' % (
                is_return,
                is_delete,
                player_trade.id,
                player_trade.from_player.pk,
                player_trade.to_player.pk,
                )
        if player_trade.status in (StaticValues.TRADE_STATUS_BIRTH, StaticValues.TRADE_STATUS_FINISH):
            #トレード成立したものは対象外
            outstr += " Skip"
            logging_method(outstr)
            continue

        trade_entries = TradeEntry.objects.filter(player_trade = player_trade)

        for te in trade_entries:
            if not te:
                continue

            s = " [TradeEntryID] %s [TradeEntryType] %s [TradeEntryKey] %s [TradeEntryValue] %s" % (
                    te.id, te.article_type, te.article_key, te.article_value)
            ret = return_item(te, message, is_return, is_delete)
            logging_method(outstr + s + " [Return] %s" % (ret))
        if is_delete:
            player_trade.delete()
        if sleep:
            sleep_sec = sleep[0]
            sleep_num = sleep[1]
            count += 1
            if count and count % sleep_num == 0:
                time.sleep(sleep_sec)

def make_test_data():
    import random
    pall=Player.objects.all()

    def make_te(player_trade, action):
        trade_entry = TradeEntry.objects.create(player_trade=player_trade, trade_action=action)
        trade_entry.article_type = random.choice(range(1,7))
        if trade_entry.article_type == StaticValues.TYPE_CARD:
            py=PlayerYakuza.objects.create(yakuza=Yakuza.get(1))
            trade_entry.article_key = py.id
            trade_entry.article_value = 1
        if trade_entry.article_type == StaticValues.TYPE_ITEM:
            trade_entry.article_key = 1
            trade_entry.article_value = 1
        if trade_entry.article_type == StaticValues.TYPE_TREASURE:
            trade_entry.article_key = 25
            trade_entry.article_value = 1
        elif trade_entry.article_type in (StaticValues.TYPE_MEDAL, StaticValues.TYPE_MONEY, StaticValues.TYPE_POINT):
            trade_entry.article_value = 1
        trade_entry.save()
        return trade_entry

    def make_data(p0, p1):
        player_trade = PlayerTrade.objects.create(from_player=p0, to_player=p1)
        make_te(player_trade, StaticValues.TRADE_ACTION_REQUEST)
        make_te(player_trade, StaticValues.TRADE_ACTION_APPROVE)

    for from_player in pall:
        to_player=random.choice(pall)
        make_data(from_player, to_player)

class Command(BaseCommand):
    help = u'''テキストに従ってTTを削除します'''
    option_list = BaseCommand.option_list + (
        make_option('--sleep',
            action='store',
            dest='sleep',
            default=False,
            help=u'一定件数ごとにスリープします。100件毎に0.5秒ならば"0.5:100"としてください'),
        make_option('--print',
            action='store_true',
            dest='print_execute',
            default=False,
            help=u'詳細な表示を行います'),
        make_option('--exec',
            action='store_true',
            dest='execute',
            default=False,
            help=u'実際に返却します'),
        make_option('--all',
            action='store_true',
            dest='return_all',
            default=False,
            help=u'全データを返却します'),
        make_option('--before48h',
            action='store_true',
            dest='return_48h',
            default=False,
            help=u'48時間以上前のデータを返却します'),
        make_option('--message',
            action='store',
            dest='message',
            default=False,
            help=u'メッセージを指定します。指定がない場合はデフォルトメッセージを使用します'),
    )

    if settings.DEBUG:
        option_list += (
                make_option('--make_dummy_data',
                    action='store_true',
                    dest='make_dummy_data',
                    default=False,
                    help=u'返却テストをします'),
        )

    def handle(self, *args, **options):
        start_time = datetime.now()
        logging_method(u'開始時間:%s' % start_time, True)

        if options.get('print_execute', False):
            global global_print_flg
            global_print_flg = True

        message = options.get('message', False)
        if not message:
            message ='取引中だったアイテムを返却させて頂きます。ご迷惑おかけ致しました。'

        player_trades = None
        if options.get('return_all', False):
            #全返却
            player_trades = PlayerTrade.objects.all()
        elif options.get('return_48h', False):
            d=datetime.today()+timedelta(days=-3)
            limit=datetime(d.year, d.month, d.day)
            player_trades = PlayerTrade.objects.filter(updated_at__lte=limit)
        elif settings.DEBUG and options.get('make_dummy_data', False):
            player_trades = PlayerTrade.objects.all()
            if not player_trades:
                make_test_data()
                logging_method(u'ダミーデータ作成しました\n', True)
            player_trades = PlayerTrade.objects.all()
            logging_method(u'テストモードです(%s件)\n' % (player_trades.count()), True)

        is_sleep = options.get('sleep', False)
        if is_sleep:
            sleep_sec = float(is_sleep.split(":")[0])
            sleep_num = int(is_sleep.split(":")[1])

        player_trades_count = player_trades.count()
        if not options.get('execute', False):
            logging_method(u'デバッグモードです(%s件)\n' % (player_trades_count), True)
            return_items(player_trades, message, [sleep_sec, sleep_num])
        else:
            logging_method(u'実際に返却を行います(%s件)\n' % (player_trades_count), True)
            return_items(player_trades, message, [sleep_sec, sleep_num], True, True)

        end_time = datetime.now()
        logging_method(u'\n実行時間:%s(%s件)' % (end_time - start_time, player_trades_count), True)
