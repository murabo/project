# -*- coding: utf-8 -*-
"""
AttributeKVSのredis versionのようなもの
AttributeKVSはsetした時点で保存されるが、
AttributeRedisはsaveを読んだ時にredisに保存される。
使い方は、tests/test_attribute.pyを参照
"""
from __future__ import with_statement
import copy

import msgpack
import redis
import gredis


class AttributeRedis(object):

    db_name = 'default'
    try_count = 1000
    attributes = {}

    class SaveError(Exception):
        def __init__(self, key):
            self.key = key

    # with文を使うと下記の順番で処理が行われる
    #「_init__() → __enter__() → 処理 → __exit__() → __del__()」の順で処理が行われる
    def __init__(self, **kwargs):
        self.db_name = kwargs.get('db_name', None) or self.db_name
        self.redis = gredis.get(self.db_name)

        self.key = ':'.join([self._key_prefix(), self.get_kvs_key(**kwargs)])

        data = self.redis.get(self.key)
        self._attributes = msgpack.unpackb(data) if data else copy.copy(self.attributes)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            return False
        self.save()
        return True
    
    def __del__(self):
        pass

    # オブジェクトクラスにあるフックメソッド。
    # オーバーライドする事で、フィールドアクセスが全てこのメソッドになる。オブジェクトコンポジション。
    def __getattr__(self, name):
        if name in self.attributes:
            return self.__dict__['_attributes'][name]
        else:
            return self.__dict__[name]

    def __setattr__(self, name, value):
        if name in self.attributes:
            self.__dict__['_attributes'][name] = value
        else:
            self.__dict__[name] = value


    def _key_prefix(self):
        return self.__class__.__name__

    def get_kvs_key(self, **kwargs):
        return ''

    def save(self):
        def f():
            return self._save()

        def e():
            raise self.SaveError(self.key)

        return self._transaction_loop(self.try_count, f, e)

    def _save(self):
        with self.redis.pipeline() as pipe:
            pipe.watch(self.key)

            save_data = pipe.get(self.key)
            save_data = self._attributes

            pipe.multi()

            pipe.set(self.key, msgpack.packb(save_data))

            pipe.execute()
        return True

    def _transaction_loop(self, count, f, e):
        try_count = 0
        while True:
            try:
                try_count += 1
                result = f()
                break
            except redis.exceptions.WatchError:
                if count < try_count:
                    e()
        return result

    def delete(self):
        """
        キーごと削除
        """
        if not self.redis:
            self.redis = gredis.get(self.db_name)
        self.redis.delete(self.key)

    def init_values(self):
        """
        値の初期化
        """
        for key,value in self._attributes.iteritems():
            self.__dict__['_attributes'][key] = value
