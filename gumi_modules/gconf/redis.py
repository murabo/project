# -*- coding: utf-8 -*-
"""
django.conf.settings.REDIS_DATABASES を使用する際,
gconf.redis.RedisSettings を使用する事.

settings.py の REDIS_DATABASES の設定例は次の通り.

.. code-block:: python

    REDIS_DATABASES = {
        'default': {
            'HOST': 'localhost',
            'PORT': '6379',
            'DB': '0',
            'MAX_CONNECTIONS': '1',
        },
        'glot': {
            'HOST': '10.0.0.1',
            'MAX_CONNECTIONS': '32',
        },
        'vlot': {},
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


Redis の接続情報だけ必要な場合は次の通り.

>>> from gconf.redis from RedisSettings
>>> settings = RedisSettings(name='default')
>>> settings.host # localhost
>>> settings.kwargs # {'host': 'localhost', 'port': 6379, 'db': 0, max_connections: 1}

RedisSettings の引数は, REDIS_DATABASES ディクショナリのキーを指定する.
引数を省略すると 'default' を渡した事となる.

kwargs() メソッドで, StrictRedis や ConnectionPool に渡す引数を取得できる.

>>> from redis import ConnectionPool
>>> kwargs = settings.kwargs
>>> pool = ConnectionPool(**kwargs)
"""

from gconf.dict import DictSettings

class RedisSettings(DictSettings):
    _default_redis_settings = {
        'HOST': 'localhost',
        'PORT': '6379',
        'DB': '0',
        'MAX_CONNECTIONS': '1',
    }

    settings_name = 'REDIS_DATABASES'
    default_settings = {
        'default': _default_redis_settings,
    }

    def __init__(self, name='default'):
        super(RedisSettings, self).__init__()
        self._redis_settings = getattr(self, name)

    def kwargs(self):
        return {'host': self.host,
                'port': self.port,
                'db': self.db,
                'max_connections': self.max_connections}

    def _get(self, name):
        return self._redis_settings.get(name, self._default_redis_settings[name])

    @property
    def host(self):
        return self._get('HOST')

    @property
    def port(self):
        return int(self._get('PORT'))

    @property
    def db(self):
        return int(self._get('DB'))

    @property
    def max_connections(self):
        return int(self._get('MAX_CONNECTIONS'))