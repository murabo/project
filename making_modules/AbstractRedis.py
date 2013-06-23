#coding:utf-8

import redis

class AbstractRedis(object):
    def __init__(self):
       self.redis = redis.Redis()

    def set(self, key, value):
        self.redis.set(key, value)

    def get(self, key):
        return self.redis.get(key)

    def rightpush(self, key, *values):
        self.redis.rpush(key, *values)

    def leftpush(self, key, *values):
        self.redis.lpush(ley, *values)

    def get_list(self, key):
        return self.redis.lrange(key, 0, -1)

    def get_list_limit(self, key, limit):
        return self.redis.lrange(key, 0, limit)

    def delete(self, key):
        self.redis.delete(key)

    def delete_all(self):
        self.redis.flushall()

    def set_transaction(self):
        self.pipe = self.redis.pipeline()
        return self.pipe

    def execute_transaction(self):
        self.pipe.execute()

    def setadd(self, key, *values):
        self.redis.sadd(key, *values)

    def setrem(self, key):
        self.redis.srem(key)

    def get_set(self, key):
        return self.redis.smembers(key)

    def sunion(self, *keys):
        return self.redis.sunionstore(*keys)

    def sinter(self, *keys):
        return self.redis.sinterstore(*keys)

    def sdiff(self, *keys):
        return self.redis.sdifstoref(*keys)

    def hmset(self, key, dict):
        self.redis.hmset(key, dict)

    def hlen(self, key):
        return self.redis.hlen(key)

    def get_keys(self, key):
        return self.redis.hkeys(key)

    def get_values(self, key):
        return self.redis.hvals(key)

    def get_dict(self, key):
        return self.redis.hgetall(key)

    def get_type(self, key):
        return self.redis.type(key)

    def sort_list_desc(self, key):
        return self.redis.sort(key, 'desc')

    def sort_list_asc(self, key):
        return self.redis.sort(key)

    def sort_stringlist_asc(self, key):
        return self.redis.sort(key, 'alpha')

    def sort_stringlist_desc(self, key):
        return self.redis.sort(key, 'alpha', 'desc')

class RankingRedis(AbstractRedis):
    def __init__(self):
        super(RankingRedis, self).__init__()

    def add(self, key, point, name):
        self.redis.zadd(key, point, name)

    def rem(self, key):
        self.redis.zrem(key)

    def get_ranking_desc(self, key):
        return self.redis.zrevrange(key, 0, -1)

    def get_ranking_asc(self, key):
        return self.redis.zrange(key, 0, -1)

    def get_ranking_by_name(self, key, name):
        return self.redis.zrank(key, name)

    def get_ranking_by_name_reverse(self, key, name):
        return self.redis.zrevrank(key, name)

