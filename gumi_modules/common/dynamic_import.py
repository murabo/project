# -*- coding: utf-8 -*-

import os
import glob
from django.core.cache import cache
from gameevent.models import GameEvent

class DynamicImport(object):
    '''
    汎用動的importクラス
    '''
    #検索対象のトップディレクトリ
    #common/dynamic_import.pyの一つ上のディレクトリ(gokudo/gokudo)
    SERVER_TOP_DIR = os.path.join(os.path.dirname(__file__), '../')

    @classmethod
    def get_cache_find_files(cls, path, key):
        return '%s:find_files:%s:%s' % (cls.__class__.__name__, path, key)

    @classmethod
    def find_files(cls, path, key, use_cache=True):
        '''
        pathの直下から、keyを含むファイル/ディレクトリを見つける
        ファイルの場所は移動することはめったにないので、24時間キャッシュする
        当然、新規追加等の場合はキャッシュをクリアすること

        キャッシュを使っている理由:
        globを使ってファイルを探しているので、コンテキストスイッチが発生する
        コンテキストスイッチは元々重い処理のなのでキャッシュを使う
        '''
        def get_file(path, key):
            files = glob.glob("%s/*" % path)
            record = [f for f in files if key in f and not ".pyc" in f]
            return record

        if not use_cache:
            return get_file(path, key)

        cache_path = cls.get_cache_find_files(path, key)
        record = cache.get(cache_path, None)
        if record is None:
            try:
                os.chdir(cls.SERVER_TOP_DIR) #検索のために位置を移動しておく
                record = get_file(path, key)
                cache.set(cache_path, record, 24*60*60) #24時間
            except cls.DoesnotExist:
                pass
        return record

    @classmethod
    def import_module(cls, from_path, import_path=None):
        '''
        動的インポート

        使い方
        from common.dynamic_import import DynamicImport
        DynamicImport.import_module("common.dynamic_import", "DynamicImport")

        from common.dynamic_import import *
        DynamicImport.import_module("common.dynamic_import")

        from eventmodule.eXXX_yakuzatree import constants as ESV
        ESV = DynamicImport.import_module("eventmodule.eXXX_yakuzatree", "constants")
        '''
        #一応'/'を'.'置き換える
        from_path = from_path.replace('/', '.')
        from_path = from_path.replace('.py', '')

        _import_path = []
        if import_path:
            _import_path.append(import_path)

        module = __import__(from_path, {}, {}, _import_path)
        if import_path:
            module = getattr(module, import_path)
        else:
            import_path = from_path.split(".")[-1]
            module = getattr(module, import_path)
        return module

class DynamicEventModuleImport(DynamicImport):
    '''
    eventmoduleの動的import

    注意:できるだけこちらを直接使わないように!!!
    DynamicEventImportを使ってください

    問題:使わないけど、eventmoduleの初期だと現在のイベントとは違いディレクトリ位置が違う、
    等の問題がある。汎用性はあまりない。
    '''
    EVENT_PATH = "eventmodule"

    @classmethod
    def find_files_by_id(cls, event_id):
        '''
        イベントIDで一覧取得する
        '''
        key = "e%s_" % str(event_id)
        try:
            #return "eventmodule/e157_yakuzatree"#super(DynamicEventModuleImport, cls).find_files(cls.EVENT_PATH, key)[0]
            return super(DynamicEventModuleImport, cls).find_files(cls.EVENT_PATH, key)[0]
        except IndexError:
            return None

    @classmethod
    def find_files_by_name(cls, name):
        '''
        イベントのディレクトリに使われる名前で取得する
        '''
        return super(DynamicEventModuleImport, cls).find_files(cls.EVENT_PATH, str(name))

    @classmethod
    def find_files_by_category(cls, category):
        '''
        イベントのカテゴリ(GameEvent.category)で取得する
        '''
        events = GameEvent.get_events_by_category(category)
        files = [cls.find_files_by_id(event.pk) for event in events]
        files = [f for f in files if f]
        return files

    @classmethod
    def get_templates_path(cls, event_path, is_mobile):
        '''
        templatesのパスを取得します

        とりあえず、固定で返す
        '''
        if is_mobile:
            path = 'templates/mobile'
        else:
            path = 'templates/smartphone'
        return '%s/%s' % (event_path, path)

    @classmethod
    def import_constants(cls, event_path, name=None):
        module = super(DynamicEventModuleImport, cls).import_module(event_path, "constants")
        if name:
            return getattr(module, name)
        return module

    @classmethod
    def import_boss_constants(cls, event_path, name=None):
        module = super(DynamicEventModuleImport, cls).import_module(event_path, "boss_constants")
        if name:
            return getattr(module, name)
        return module

    @classmethod
    def import_decorators(cls, event_path, name):
        path = "%s.decorators" % event_path
        return super(DynamicEventModuleImport, cls).import_module(path, name)

    @classmethod
    def import_base_utils(cls, event_path, name):
        #ID:140などの古いのではディレクトリ構成が違うので使えない...
        #TODO:汎用化をどこまでするか?
        path = "%s.utils.base_utils" % event_path
        return super(DynamicEventModuleImport, cls).import_module(path, name)

    @classmethod
    def import_actionlog_util(cls, event_path, name):
        path = "%s.utils.actionlog_util" % event_path
        return super(DynamicEventModuleImport, cls).import_module(path, name)

class DynamicEventImport(DynamicEventModuleImport):
    '''
    イベントの動的import

    外部から使う場合はこちらを使うこと
    eventmodule自体が将来的に変更を目標に入れているので、DynamicEventModuleImportを継承している
    実装が変われば、新しいクラスを作成し、継承元を変更して対応すること
    '''
    pass
