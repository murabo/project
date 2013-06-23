# -*- coding: utf-8 -*-
"""
redis.ConnectionPool は, 同時接続数が最大接続数を超えると例外が発生する.

そこで, セマフォを利用してプーリングされている接続が空くまで待つ
ConnectionPool Class を提供する.

>>> import redis
>>> from gredis.pool import ConnectionPool
>>> pool = ConnectionPool(max_connections=10)
>>> r = redis.StrictRedis(connection_pool=pool)

Redis-py のバージョンが上がる際に必ず動作確認(テスト)を行う事.
2.6.2, 2.7.2 テスト済み.

普段は, gredis.get() や gredis.get_pool() を使用する事.
"""
import sys
import threading
import redis

class ConnectionPool(redis.ConnectionPool):
    def __init__(self, *args, **kwargs):
        super(ConnectionPool, self).__init__(*args, **kwargs)
        self._sem = threading.BoundedSemaphore(value=self.max_connections)

    def get_connection(self, *args, **kwargs):
        self._sem.acquire()
        try:
            return super(ConnectionPool, self).get_connection(*args, **kwargs)
        except:
            self._sem.release()
            raise

    def release(self, connection):
        super(ConnectionPool, self).release(connection)
        if connection.pid == self.pid:
            try:
                self._sem.release()
            except ValueError:
                pass # 過剰 release は握りつぶす
