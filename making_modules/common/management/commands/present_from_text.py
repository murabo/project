# -*- coding: utf-8 -*-

"""
テキストデータを元にプレゼントを行う(主に補償用)

入力テキストデータ仕様
ファイル形式はデフォルトでtsv("\t" or "\s"区切り)unixコマンドとの親和性が高いため)
csvもオプションで対応

このような形式になります。
----
osuser_id type id num message
----

typeはcommo/static_valuesのStaticValues.TYPE_CARDあたりを参照してください
idは対応したIDになります

ただし、銭、レア代紋はidは使いませんので無視します。numを使用してください
"""

import sys
import datetime
import time
from optparse import make_option
from django.core.management.base import BaseCommand
from player.models import Player
from present.models import PlayerPresent
from common.article_proxy import ArticleProxy
from common.actionlog_utils import ActionLogUtils
from common.inspector_utils import InspectorLogUtils

def logging_method(message, print_flg=True):
    if not print_flg:
        return
    message = "%s" % (message)
    try:
        sys.stdout.write('%s\n' % message.encode('utf-8','ignore'))
        sys.stdout.flush()
    except:
        print message

def send_present(line, send_message=False, csv_mode=False, send_flg=False, print_flg=False):
    line = line.rstrip()
    if csv_mode:
        data = line.split(",")
    else:
        data = line.split()
    if len(data) != 4 and len(data) != 5:
        logging_method("skip:入力値異常です %s" % line, print_flg)
        return False

    osuser_id = int(data[0])
    send_type = int(data[1])
    send_id = int(data[2])
    send_num = int(data[3])
    if send_message:
        message = send_message
    elif len(data) == 5 and len(data[4]) > 0:
        #メッセージの指定
        message = data[4]
    else:
        #デフォルトメッセージ
        message = u'この度はご迷惑をおかけしました。お詫びのｱｲﾃﾑです。'

    try:
        message = message.decode('utf_8')
    except:
        pass

    player = Player.get(osuser_id)
    if not player:
        logging_method("skip:プレイヤーが存在しません %s" % line, print_flg)
        return False

    #プレゼントする
    if ArticleProxy.is_article(send_type):
        obj = ArticleProxy.get_object(send_type, send_id)
        if not obj:
            logging_method("skip:データID異常です %s" % line, print_flg)
            return False
        if send_flg:
            ActionLogUtils.write_give_compensation_present_log(player, obj, message, send_type, send_num)
            PlayerPresent.give_official_present_admin(player, obj, message, num=send_num, type=send_type)
            inspector_rarity = 0
            if ArticleProxy.is_card(send_type):
                inspector_rarity = obj.rarity
            InspectorLogUtils.write_create_log(player, [(send_type, send_id, inspector_rarity, send_num)], InspectorLogUtils.REASON_PRESENT, 'PRESENT_COMMAND')
    elif ArticleProxy.is_num(send_type):
        if send_flg:
            ActionLogUtils.write_give_compensation_present_log(player, send_num, message, send_type, send_num)
            PlayerPresent.give_official_present(player, send_num, message, type=send_type)
            InspectorLogUtils.write_create_log(player, [(send_type, send_id, 0, send_num)], InspectorLogUtils.REASON_PRESENT, 'PRESENT_COMMAND')
    else:
        logging_method("skip:データタイプ異常です %s" % line, print_flg)
        return False

    present_name = ArticleProxy.name(send_type, send_id)
    msg = u"is_send %s ouser_id %s name %s type %s id %s count %s message %s" % (send_flg, osuser_id, present_name, send_type, send_id, send_num, message)
    logging_method(msg, print_flg)
    return {"player":player, "send_type":send_type, "send_id":send_id, "send_num":send_num, "message":message}

class Command(BaseCommand):
    help = u'''テキストに従ってプレゼントを配布します'''
    option_list = BaseCommand.option_list + (
        make_option('--csv',
            action='store_true',
            dest='csv_mode',
            default=False,
            help=u'入力ファイルをCSVで読み込みます(デフォルトはTSVです)'),
        make_option('--max_num',
            action='store',
            dest='max_num',
            default=0,
            help=u'最大処理件数を指定します。送信結果は関係ありません'),
        make_option('--message',
            action='store',
            dest='message',
            default=False,
            help=u'プレゼント時のメッセージを指定します。ファイルの指定を無視します'),
        make_option('--sleep',
            action='store',
            dest='sleep',
            default=False,
            help=u'一定件数ごとにスリープします。100件毎に0.5秒ならば"0.5:100"としてください'),
        make_option('--send',
            action='store_true',
            dest='send_execute',
            default=False,
            help=u'実際に配布します'),
    )

    def handle(self, *args, **options):
        if not options.get('send_execute', False):
            logging_method(u'デバッグモードです')
        d0 = datetime.datetime.today()
        time_str = d0.strftime("%Y-%m-%d %H:%M:%S")
        logging_method(u'%s プレゼント送付開始します\n' % (time_str))

        filename = args[0]
        f=open(filename, "r")

        max_num = options.get('max_num', 0)
        max_num = int(max_num)
        count = 0

        is_sleep = options.get('sleep', False)
        if is_sleep:
            sleep_sec = float(is_sleep.split(":")[0])
            sleep_num = int(is_sleep.split(":")[1])
        while True:
            line = f.readline()
            if max_num > 0 and max_num <= count:
                break
            if len(line) == 0:
                break

            csv_mode = options.get('csv_mode', False)
            send_execute = options.get('send_execute', False)
            message = options.get('message', False)
            send_present(line, send_message=message, csv_mode=csv_mode, send_flg=send_execute, print_flg=True)
            count += 1
            if is_sleep and count and count % sleep_num == 0:
                time.sleep(sleep_sec)

        logging_method('')
        d1 = datetime.datetime.today()
        time_str = d1.strftime("%Y-%m-%d %H:%M:%S")
        logging_method(u'%s プレゼント送付終了しました' % (time_str))
        if not options.get('send_execute', False):
            logging_method(u'デバッグモードです')

        time_str = str(d1-d0)
        logging_method(u'実行時間:%s' % (time_str))
