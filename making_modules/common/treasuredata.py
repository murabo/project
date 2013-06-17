# -*- coding: utf-8 -*-

import logging
import re
import time
import logging
from django.utils import simplejson as json

from fluent import sender
from fluent import event


class TDLogger(object):
    CATEGORY_GACHA = 1
    CATEGORY_SHOP = 2
    CATEGORY_RENTALBOX = 3
    CATEGORY = {CATEGORY_GACHA:u'ガチャ',
                CATEGORY_SHOP: u'ショップ',
                CATEGORY_RENTALBOX: u'レンタル事務所',
                }

    def __init__(self, database, host='localhost', port=24224):
        self.database = database
        sender.setup('td', host=host, port=port)

    # ステータスアップデート用に新しく追加されました
    def update_status(self, uid, status, value):
        record = { 'uid': uid, 'value': value }
        tag = "%s.%s_status" % (self.database, status)
        event.Event(tag, record, time=int(time.time()))

    def add(self, action, record):
        record['action'] = action
        tag = "%s.%s" % (self.database, action)
        print "TD_LOG: %s,%s" % (action, json.dumps(record))
        logging.debug("TD_LOG: %s,%s" % (action, json.dumps(record)))
        event.Event(tag, record, time=int(time.time()))

    def register(self, uid):
        self.add('register', {'uid': uid})

    def login(self, uid):
        self.add('login', {'uid': uid})

    def pay(self, uid, category, sub_category, name, price, count):
        self.add('pay', {
            'uid': uid,
            'category': category,
            'sub_category': sub_category,
            'name': name,
            'price': price,
            'count': count
        })

    def action(self, action, uid, record):
        record['uid'] = uid
        if re.search(r'[^0-9a-z_]', action) or len(action) > 32 or len(action) < 3:
            logging.error("TD_ERROR_LOG: %s,%s,%s" % (action, uid, json.dumps(record)))
            return
        self.add(action, record)
