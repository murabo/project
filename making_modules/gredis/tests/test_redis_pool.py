# -*- coding: utf-8 -*-
"""
gredis.pool のテスト

localhost で Redis が起動していない場合は skip する.
"""

import unittest
import redis

from gredis.pool import ConnectionPool
from gredis.tests import is_redis_running, run_threads

class TestPool(unittest.TestCase):
    def setUp(self):
        self.kwargs = {
            'threads': 30,
            'incr': 300,
            'key': 'spam',
        }
        self.expr = self.kwargs['threads'] * self.kwargs['incr']

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_pipe(self):
        key = self.kwargs['key']

        pool = ConnectionPool(max_connections=2)
        r = redis.StrictRedis(connection_pool=pool)
        r.delete(key)

        run_threads(r=r, **self.kwargs)

        self.assertEqual(int(r.get(key)), self.expr)
        r.delete(key)
