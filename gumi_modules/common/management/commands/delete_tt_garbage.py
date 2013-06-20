# -*- coding: utf-8 -*-
"""
不要なTTのレコードを削除する


※消さないで対象だけ出力する
$ python manage.py delete_tt_garbage --nd=nodel.txt --d=del.txt --settings=settings_gree_production

※実際に消す
$ python manage.py delete_tt_garbage execute --nd=nodel.txt --d=del.txt --settings=settings_gree_production

※件数を指定して対象だけ出力
$ python manage.py delete_tt_garbage --l=100 --s=0 --nd=nodel.txt --d=del.txt --settings=settings_gree_production
"""

import re
import time
from django.core.management.base import BaseCommand
from optparse import make_option
from tokyotyrant import tt_operator

# TokyoTyrantのクライアントはこう書くしかないかなぁ
TT_CLIENT = tt_operator

# スリープをいれるループ間隔
SLEEP_LOOP = 10

class AppStatus(object):
    _shared_state = {}
    def __new__(cls, *a, **kw):
        instance = object.__new__(cls, *a, **kw)
        instance.__dict__ = cls._shared_state
        return instance

class Command(BaseCommand):
    help = u'''不要なTTのレコードを削除する'''
    option_list = BaseCommand.option_list + (
        make_option('--nd',
            action='store',
            dest='nodeletelist',
            help=u'削除しないキーの正規表現リスト（改行区切り）'),
        make_option('--d',
            action='store',
            dest='deletelist',
            help=u'削除するキーの正規表現リスト（改行区切り）'),
        make_option('--l',
            action='store',
            dest='limit',
            default=None,
            help=u'削除する数'),
        make_option('--s',
            action='store',
            dest='sleeptime',
            default=200,
            help=u'%sループごとのスリープ時間' % SLEEP_LOOP),
    )

    def handle(self, *args, **options):
        status = AppStatus()

        status.is_delete = False
        if len(args) == 1:
            if args[0] == 'execute':
                status.is_delete = True
        
        status.limit = options.get('limit', None)
        status.verbosity = int(options.get('verbosity', None))
        status.sleep_time = int(options.get('sleeptime', None)) / 1000.0
        nodelete_list_path = options.get('nodeletelist', None)
        delete_list_path = options.get('deletelist', None)
        if not nodelete_list_path or not delete_list_path:
            print 'error. files is not specified.'
            return

        nodelete_list = file_to_list(nodelete_list_path)
        delete_list = file_to_list(delete_list_path)
        delete_garbage(TT_CLIENT, nodelete_list, delete_list)
        print 'finished.'


def file_to_list(file):
    'ファイルを改行区切りでリストにセット'
    f = open(file, 'r')
    list = []
    for line in f:
        val = line.split('\n')[0]
        if val:
            list.append(val)
    return list

def match_keynamelist(keyname, reg_keynames):
    '正規表現で書かれたキー名リストとマッチするか'
    for reg_keyname in reg_keynames:
        p = re.compile(reg_keyname)
        if p.match(keyname):
            return True
    return False

def delete_keyvalue(tt, key):
    'KVSを消す'
    status = AppStatus()
    if status.is_delete:
        '本当に消す'
        tt.out(key)
        if status.verbosity >= 2:
            print '!!!deleted!!!'

def delete_garbage(tt, nodelete_list, delete_list):
    'リストを取得するループ'
    status = AppStatus()
    tt.iterinit()
    del_count = 0
    i = 0
    while True:
        if status.limit and del_count >= int(status.limit):
            break
        try:
            key = tt.iternext()
            if not key:
                return True
            if match_keynamelist(key, nodelete_list):
                '消さないキー名にマッチ'
                if status.verbosity >= 2:
                    print '# skip ###########: %s' % key
                continue
            if match_keynamelist(key, delete_list):
                '消すキー名にマッチ'
                delete_keyvalue(tt, key)
                print key
                del_count += 1
        except:
            return False
        i += 1
        if i % SLEEP_LOOP == 0:
            time.sleep(status.sleep_time)
    return True
