# -*- coding: utf-8 -*-

import unittest

from gredis.attribute import AttributeRedis
from gredis.tests import is_redis_running


class TestAttribute(AttributeRedis):

    attributes = {
        'player_id': '100000',
        'yakuza_ids': [1000, 1, 2, 4, 5]
    }

    def __init__(self, **kwargs):
        super(TestAttribute, self).__init__(**kwargs)


class TestAttributeRedis(unittest.TestCase):
    def setUp(self):
        self.ta = TestAttribute()

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_key(self):
        self.assertEqual(self.ta.key, 'TestAttribute:')

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_set_and_get(self):
        player_id = self.ta.player_id
        yakuza_ids = self.ta.yakuza_ids
        self.ta.player_id = '10000000'
        self.assertNotEqual(self.ta.player_id, player_id)
        self.assertEqual(self.ta.yakuza_ids, yakuza_ids)

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_save(self):
        self.ta.player_id = '100001'
        self.ta.save()
        ta = TestAttribute()
        self.assertEqual(self.ta.player_id, ta.player_id)
        self.assertEqual(self.ta.yakuza_ids, list(ta.yakuza_ids))

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_with(self):
        with TestAttribute() as ta:
            self.assertEqual(type(ta), TestAttribute)
            ta.player_id = '1'
            ta.yakuza_ids = [1000, 2000, 3000]

        after_ta = TestAttribute()
        self.assertEqual('1', after_ta.player_id)
        self.assertEqual([1000, 2000, 3000], list(after_ta.yakuza_ids))

    @unittest.skipUnless(is_redis_running(), 'Redis Server is not running on localhost')
    def test_delete(self):
        attributes = self.ta._attributes
        self.ta.delete()
        ta = TestAttribute()
        self.assertEqual(ta._attributes, TestAttribute.attributes)
        self.assertNotEqual(ta._attributes, attributes)
