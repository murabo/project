#coding:utf-8

from __future__ import with_statement
import gredis


'''
redisを仕様するための基本的なメソッドを搭載
'''
class AbstractRedis(object):
    def __init__(self):
       self.redis = gredis.get()
    
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


class RankingRedis(AbstractRedis):
    def __init__(self):
        super(RankingRedis, self).__init__()

    def register(self, key, point, name):
        self.redis.zadd(key, point, name)

    def unregister(self, key):
        self.redis.zrem(key)

    def get_ranking(self, key):
        return self.redis.zrevrange(key, 0, -1)

    def get_ranking_reverse(self, key):
        return self.redis.zrange(key, 0, -1)

    def get_ranking_by_name(self, key, name):
        return self.redis.zrank(key, name)

    def get_ranking_by_name_reverse(self, key, name):
        return self.redis.zrevrank(key, name)

