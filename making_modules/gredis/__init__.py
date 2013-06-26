# -*- coding: utf-8 -*-
"""
Redis Client を取得する.
取得した Redis Client は, Thread-safe に Connection Pooling されている.

利用方法は次の通り.

>>> import gredis
>>> r = gredis.get(name='spam')
>>> r.get('ham')

get() の引数 name には, django.conf.settings.REDIS_DATABASES のキー名を指定する.
django.conf の import に失敗した場合, キー名 'default' だけは自動定義される.
Django Settings の記載例は次の通り.

.. code-block:: python

    REDIS_DATABASES = {
        'default': {
            'HOST': '10.0.0.1',
            'PORT': '6379',
            'DB': '0',
            'MAX_CONNECTIONS': '10',
        },
        'glot': {
            'HOST': '10.0.0.2',
            'MAX_CONNECTIONS': 1,
        },
        'vlot': {}
    }


HOST
    Redis Server の IP アドレス.
    省略すると 'localhost' が使用される.

PORT
    Redis Server の IP アドレス.
    省略すると '6379' が使用される.
    str もしくは int 型で指定する事.

DB
    Redis Server の DB 番号. (同一 Redis Server 内で DB を指定できる)
    省略すると '0' が使用される.
    str もしくは int 型で指定する事.

MAX_CONNECTIONS
    Redis Server への同時接続数.
    省略すると '1' が使用される.
    str もしくは int 型で指定する事.
    set や get 等のコマンドを同時に発行できる数であり, 同時発行数を超えた場合,
    他のコマンドの発行が終わるまで待つ事になる.


django.conf.settings.REDIS_DATABASES に存在しないキー名を get() に渡すと
raise が発生するため, 前述の例では 'vlot' の為に空 dict を指定している.
"""
from __future__ import with_statement
import threading
import redis

from gredis.gconf.redis import RedisSettings
from gredis.pool import ConnectionPool

_LOCK = threading.Lock()
_POOL = {}
_CLIENT = threading.local()

def get(name='default'):
    """
    Redis client を取得する.
    Connection は, get_pool() を利用して取得している.

    Redis client は Thread 毎に持つが, Redis connection pool は Process 毎に持つ.
    """
    global _CLIENT
    print 1
    client = getattr(_CLIENT, name, None)
    if client is not None:
        print 'e1'
        return client
    print 2
    client = redis.StrictRedis(connection_pool=get_pool(name))
    setattr(_CLIENT, name, client)
    print 3
    return client

def get_pool(name='default'):
    """
    Redis connection pool を取得する.

    get() の中で使用されている.
    """
    global _POOL
    print 4
    print _POOL
    if _POOL.get(name):
         print 'e4'
         return _POOL[name]
    print 5
    return _set_and_get_pool(name)

def _set_and_get_pool(name):
    global _LOCK
    global _POOL
    print 6
    with _LOCK:
        if _POOL.get(name):
            print 'e6'
            return _POOL[name]
        print 7
        kwargs = RedisSettings(name).kwargs()
        print 8
        print kwargs
        _POOL[name] = ConnectionPool(**kwargs)
        print 9
        print _POOL[name]
        return _POOL[name]
