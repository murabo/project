# -*- coding: utf-8 -*-

"""
TTの掃除スクリプト

ファイルから削除したいTTを指定する。ファイルはDSLっぽくかけるようにする。


class Plaeyr
    @classmethod
    def _get_level_player_key(cls, level):
        return '%s:level%d' % (cls._meta, level)
    @classmethod
    def get_level_player_ids(cls, level):
        return tt_operator.get_list(cls._get_level_player_key(level))

    def _get_place_yakuza_key(self, place, yakuza):
        return '%s:%s:get_place:%s:yakuza:%s' % (self._meta, self.pk, place.pk, yakuza.pk)
    def _get_place_yakuza(self, place, yakuza):
        return tt_operator.getint(self._get_place_yakuza_key(place, yakuza))

というTTがある場合

以下のようにファイルに書く。
from tokyotyrant import tt_operator
from player.models import Player
from place.models import PlayerPlace
from yakuza.models import Yakuza

TTDelete(tt_operator)[
    ('%s:level%s', Player._meta, [1..149]),
    ('%s:%s:get_place:%s:yakuza:%s', Player._meta, Player.objects.all(), PlayerPlace.objects.all(), Yakuza.objects.all()),
]

一般化すると以下の様な形式となります。
TTDelete(TT_OPERATOR)[
    (KEY_STRING, KEY_STRING_VALUE1, [KEY_STRING_VALUE2, ....]),
    ...,
]

注意事項
1:exec()を使用します。当然ながら、typo等には気をつけてください。
2:必要なimportはファイルに書いてください。
3:削除するのは、tokyotyrant/__init__.pyのtt_*が対象です。
4:最初の引数のフォーマット文字列では%sを使用してください
5:本番DBを使用したくない場合は、objects.using('other')をしてレプリケーションを見るようにしてください。
6:ローカルテストでデータの削除できない場合があった。原因は不明。

TTのキー追加/削除確認方法
TTモジュール(tokyotyrant/*)では一覧表示は未サポート?なので、tcrmgrを使う
$ tcrmgr list -port 2021 127.0.0.1                  #キー一覧表示
$ tcrmgr list -port 2021 -fm "key_string" 127.0.0.1 #接頭語を指定してキー一覧表示
"""

import sys
import os
import time
import datetime
import thread
import copy
from optparse import make_option
from django.core.management.base import BaseCommand
#from common.actionlog_utils import ActionLogUtils

#exec()使用している関係でフラグ系はグローバル変数で管理
global_print_flg = False
global_exec_flg = False

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

thread_alive_flg = False # is dead thread?
def tt_out_thread(tt_obj, rpipe):
    "This thread is execute tt.out()"
    global thread_alive_flg
    global global_exec_flg

    rpipe = os.fdopen(rpipe, 'r')
    if not tt_obj:
        logging_method("Error:tt_obj is None")
        return

    count = 0

    while True:
        tt_key = rpipe.readline()
        tt_key = tt_key.strip()
        if len(tt_key) == 0:
            break
        if global_exec_flg:
            tt_obj.out(tt_key)
        logging_method("%s.out(%s)" % (str(tt_obj), tt_key))
        count += 1
        if count % 1000 == 0:
            time.sleep(0.5)
    thread_alive_flg = True

class TTDelete(object):
    def __init__(self, tt_obj):
        global thread_alive_flg
        thread_alive_flg = False

        self.tt_obj = tt_obj
        rpipe, wpipe = os.pipe()
        self.wpipe = os.fdopen(wpipe, 'w')
        thread.start_new_thread(tt_out_thread, (tt_obj, rpipe))

    def __walk_combination(self, args):
        def combination(lis, args):
            if len(args) == 0:
                tt_key = lis[0]%tuple(lis[1:])
                self.wpipe.write(tt_key+"\n")
                return
            else:
                if not hasattr(args[0], '__iter__'): #iterable?
                    tmp=lis
                    tmp.append(str(args[0]))
                    combination(lis, args[1:])
                else:
                    for val in args[0]:
                        tmp=copy.copy(lis)
                        tmp.append(str(val))
                        combination(tmp, args[1:])

        start_time = datetime.datetime.now()
        logging_method('start:%s:\"%s\"' % (start_time, args[0]), True)
        combination([args[0]], args[1:])

    def __getitem__(self, args):
        for arg in args:
            if not isinstance(arg, tuple) and isinstance(arg, list):
                continue
            try:
                self.__walk_combination(arg)
            except KeyboardInterrupt:
                logging_method('\nCatch:Ctrl-C', True)
                break

        self.wpipe.close()
        global thread_alive_flg
        while True:
            if thread_alive_flg:
                break
            time.sleep(1)

class Command(BaseCommand):
    help = u'''テキストに従ってTTを削除します'''
    option_list = BaseCommand.option_list + (
        #TODO:必要だったら対応する
        #make_option('--sleep',
        #    action='store',
        #    dest='sleep',
        #    default=False,
        #    help=u'一定件数ごとにスリープします。100件毎に0.5秒ならば"0.5:100"としてください'),
        make_option('--print',
            action='store_true',
            dest='print_execute',
            default=False,
            help=u'詳細な表示を行います'),
        make_option('--exec',
            action='store_true',
            dest='execute',
            default=False,
            help=u'実際に削除します'),
    )

    def handle(self, *args, **options):
        global global_print_flg
        global global_exec_flg

        start_time = datetime.datetime.now()
        logging_method(u'開始時間:%s' % start_time, True)

        if not options.get('execute', False):
            logging_method(u'デバッグモードです', True)
        else:
            global_exec_flg = True

        if options.get('print_execute', False):
            global_print_flg = True

        filename = args[0]
        f=open(filename, "r")
        file_data = f.read()
        f.close()

        exec(file_data)

        end_time = datetime.datetime.now()
        logging_method(u'実行時間:%s' % (end_time - start_time), True)
