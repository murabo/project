# coding: utf-8
from __future__ import absolute_import, with_statement

from common.redis.mixins.client import RedisMixin

import msgpack

__all__ = ['get_cache', 'cache']


class Cache(RedisMixin):

    def __init__(self, name='default'):
        self.redis_name = name

    def get(self, key, default=None):
        _v = self.redis.get(key)
        if not _v:
            return default
        return msgpack.unpackb(_v)

    def get_many(self, keys):
        d = {}
        values = self.redis.mget(keys)
        d = dict([(key, msgpack.unpackb(values[i])) for i, key in enumerate(keys)])
        return d 

    def set(self, key, value, timeout=3600):
        _value = msgpack.packb(value)
        return self.redis.setex(key, timeout, _value)

    def set_many(self, d={}, timeout=3600):
        with self.redis.pipeline() as pipe:
            pipe.multi()
            for k, v in d.items():
                _v = msgpack.packb(v)
                pipe.setex(k, timeout, _v)
            pipe.execute()

    def delete(self, key):
        return self.redis.delete(key)


def get_cache(name='default'):
    return Cache(name)

cache = get_cache()
