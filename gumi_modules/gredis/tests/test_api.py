# -*- coding: utf-8 -*-
"""
gredis のテスト

localhost で Redis が起動していない場合は skip する.
"""

import unittest
import redis
import threading

from gredis import get, get_pool
from gredis.pool import ConnectionPool
from gredis.tests import is_redis_running, run_threads

class GetThread(threading.Thread):
    def run(self):
        self.r = get()


class GetPoolThread(threading.Thread):
    def run(self):
        self.pool = get_pool()


class TestPool(unittest.TestCase):
    def setUp(self):
        self.kwargs = {
            'threads': 10,
            'incr': 300,
            'key': 'spam',
        }
        self.expr = self.kwargs['threads'] * self.kwargs['incr']

    def test_get(self):
        ts = [GetThread() for i in xrange(0, 100)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()

        for t in ts:
            self.assertIsInstance(t.r, redis.StrictRedis)

    def test_get_pool(self):
        ts = [GetPoolThread() for i in xrange(0, 100)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()

        expr = ts[0].pool
        self.assertIsInstance(expr, ConnectionPool)
        for t in ts:
            self.assertEqual(t.pool, expr)

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_pipe(self):
        key = self.kwargs['key']

        r = get()
        r.delete(key)

        run_threads(r=r, **self.kwargs)

        self.assertEqual(int(r.get(key)), self.expr)
        r.delete(key)
