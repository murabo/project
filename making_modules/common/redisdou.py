# -*- coding: utf-8 -*-

import redis
from redis.exceptions import ConnectionError
# from nose.tools import ok_, eq_

class Redisdou:
    HOST    = {
        'RECORD': 'gokudo-redis01.gu3.jp',
        'MASTER': 'gokudo-redis02.gu3.jp',
        'SLAVES': ('gokudo-redis03.gu3.jp', 'gokudo-redis04.gu3.jp', 'gokudo-redis05.gu3.jp',)
    }

    def __init__(self, userid, value_size=100, port=6379):
        self._userid        = str(userid)
        self._value_size    = value_size
        self._slave_no      = None

        self._connect(port)

    def _connect(self, port=6379):
        '''
        各種 Redis に接続する。
        port 指定は基本的には不要 (主にテスト用)
        '''
        #TODO: Round robin 方式に変更すること
        sum = 0
        for it in self.userid:
            sum = ord(it)
        self._slave_no      = sum % self.slave_cnt

        self._redis_record  = redis.Redis(host=self.HOST['RECORD'], port=port, db=0, socket_timeout=.2)
        self._redis_master  = redis.Redis(host=self.HOST['MASTER'], port=port, db=0, socket_timeout=.2)
        self._redis_slave   = redis.Redis(host=self.HOST['SLAVES'][self._slave_no], port=port, db=0, socket_timeout=.2)

    def write_one(self):
        key     = self.userid + '_test'
        value   = 'Z' * self._value_size

        try:
            self._redis_master.set(key, value)
            if self._redis_slave.get(key) != value:
                raise AttributeError('Slave\'s value is invalid.')
        except ConnectionError:
            self._error = 1
            return False
        except AttributeError:
            self._error = 2
            return False
        except:
            self._error = 99
            return False

        return True

    def reset(self):
        '''
        テストで使った Redis を全部消す。
        Unit Test 用なので、実務では呼んではいけない…。
        '''
        redis.Redis(host=self.HOST['RECORD'], db=0).flushdb()
        redis.Redis(host=self.HOST['MASTER'], db=0).flushdb()
        for it in self.HOST['SLAVES']:
            redis.Redis(host=it, db=0).flushdb()

    def _get_userid(self):
        return self._userid

    def _get_slave_no(self):
        return self._slave_no

    def _get_slave_cnt(self):
        return len(self.HOST['SLAVES'])

    def _get_error(self):
        return self._error

    error       = property(_get_error)
    userid      = property(_get_userid)
    slave_no    = property(_get_slave_no)
    slave_cnt   = property(_get_slave_cnt)


# class TestRedisdou:
#     def teardown(self):
#         Redisdou('dummy').reset()

#     def test_is_initialize01(self):
#         '''
#         オブジェクト初期状態は、スレーブ番号が None であること
#         '''
#         obj = Redisdou('dummy')
#         ok_(obj.slave_no > 0)

#     def test_connect01(self):
#         '''
#         スレーブ no が割り振られていること
#         '''
#         obj = Redisdou('1')
#         eq_(1, obj.slave_no)

#     def test_connect02(self):
#         '''
#         スレーブが切り替わること
#         '''
#         for i in range(10):
#             obj = Redisdou(i)
#             eq_(i % obj.slave_cnt, obj.slave_no)

#     def test_write_one01(self):
#         '''
#         ダミーデータを書き込みを行い、正常時に True が戻ること
#         '''
#         obj = Redisdou(1)
#         ok_(obj.write_one(), '正常時に True が戻ること')

#     def test_write_one02(self):
#         '''
#         接続できない Redis に書き込みを行えば False が戻ること
#         '''
#         obj = Redisdou(1, 100, 22222)
#         ok_(not obj.write_one(), '書き込み不可能で False が戻ること')
#         eq_(1, obj.error)

#         obj = Redisdou(1, 100, 99999)
#         ok_(not obj.write_one(), '書き込み不可能で False が戻ること')
#         eq_(99, obj.error)

#     def test_slave_cnt(self):
#         '''
#         スレーブの数を取得できること
#         '''
#         obj = Redisdou('dummy')
#         eq_(3, obj.slave_cnt)

#     def test_userid01(self):
#         '''
#         ユーザー id を取得できること
#         '''
#         USERID = 'aabb3355'
#         obj = Redisdou(USERID)
#         eq_(USERID, obj.userid)
