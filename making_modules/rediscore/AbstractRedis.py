# -*- coding: utf-8 -*-

"""
redisを使用するための抽象クラス。
Singletonパターンで実装されている。
基本非同期であり、saveを読んだ時にredisに保存される。
redis使用時は原則として、このクラスを継承すること。
"""

from __future__ import with_statement
import copy
import msgpack
from RedisAPI import RedisAPI

class AbstractRedis(object):

    _instance = None
    db_name = 'default'
    try_count = 1000
    attributes = {}

    class SaveError(Exception):
        def __init__(self, key):
            self.key = key

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, **kwargs):
        self.db_name = kwargs.get('db_name', None) or self.db_name
        self.redisapi= RedisAPI(self.db_name)

        self.key = ':'.join([self._key_prefix(), self.get_kvs_key()])

        data = self.redisapi.get(self.key)
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

    def get_kvs_key(self):
        return ''

    def create_subkey(self, id=1):
        subkey = '%s:sub:%s' % (self.key, id)
        while self.redisapi.redis.exists(subkey):
            id += 1
            subkey = '%s:sub:%s' % (self.key, id)   
            if id > 10:
                raise
        return '%s:sub:%s' % (self.key, id)

    def save(self):
        def f():
            return self._save()

        def e():
            raise self.SaveError(self.key)

        return self._transaction_loop(self.try_count, f, e)

    def _save(self):
        with self.redisapi.redis.pipeline() as pipe:
            pipe.watch(self.key)
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
            except self.redisapi.redis.exceptions.WatchError:
                if count < try_count:
                    e()
        return result


    def init_values(self):
        """
        値の初期化
        """
        for key,value in self._attributes.iteritems():
            self.__dict__['_attributes'][key] = value

    def delete_self(self):
        """
        任意のキー１つのキーと値を削除
        """
        self.redisapi.delete(self.key)

    def delete_all(self, db_name='default'):
        """
        任意の子クラスが所持している全キーと値を削除
        params: db_name <string> settingsに書いている名前
        """
        key = ':'.join([self.cls.__name__, '*'])
        keys = self.redisapi.redis.keys(key)
        with self.redisapi.redis.pipeline(transaction=False) as pipe:
            for key in keys:
                pipe.delete(key)
            pipe.execute()
