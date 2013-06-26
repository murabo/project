#coding:utf-8

from __future__ import with_statement
import gredis


'''
redisを仕様するための基本的なメソッドを搭載
'''

class RedisAPI(object):
    def __init__(self, db_name='default'):
        self.redis = gredis.get(db_name)

    '''
    文字列型
    '''
    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key)

    '''
    list型
    '''
    def append(self, key, values):
        if isinstance(values, list):
            with self.redis.pipeline() as pipe:
                pipe.multi()
                for value in values:
                    pipe.rpush(key, value)
                pipe.execute()
        else:
            self.redis.rpush(key, values)

    def leftappend(self, key, values):
        if isinstance(values, list):
            with self.redis.pipeline() as pipe:
                pipe.multi()
                for value in values:
                    pipe.lpush(key, value)
                pipe.execute()
        else:
            self.redis.lpush(key, values)

    def get_list(self, key, index=0, limit=-1):
        return self.redis.lrange(key, index, limit)

    def get_list_asc(self, key):
        return self.redis.sort(key, alpha=True)

    def get_list_desc(self, key):
        return self.redis.sort(key, alpha=True, desc=True)

    '''
    dict型
    '''
    def set_dict(self, key, dict):
        self.redis.hmset(key, dict)

    def get_dict(self, key):
        return self.redis.hgetall(key)

    def get_keys(self, key):
        return self.redis.hkeys(key)

    def get_values(self, key):
        return self.redis.hvals(key)

    '''
    その他
    '''
    def delete(self, key):
        self.redis.delete(key)