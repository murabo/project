#coding:utf-8

import redis

class AbstractRedis(object):
    def __init__(self):
       self.cli = redis.Redis()

    def set(self, key, value):
        self.cli.set(key, value)

    def get(self, key):
        return self.cli.get(key)

    def rightpush(self, key, *values):
        self.cli.rpush(key, *values)

    def leftpush(self, key, *values):
        self.cli.lpush(ley, *values)

    def get_list(self, key):
        return self.cli.lrange(key, 0, -1)

    def get_list_limit(self, key, limit):
        return self.cli.lrange(key, 0, limit)

    def delete(self, key):
        self.cli.delete(key)

    def set_transaction(self):
        self.pipe = self.cli.pipeline()
        return self.pipe

    def execute_transaction(self):
        self.pipe.execute()

    def setadd(self, key, *values):
        self.cli.sadd(key, *values)

    def setrem(self, key):
        self.cli.srem(key)

    def get_set(self, key):
        return self.cli.smembers(key)

    def sunion(self, *keys):
        return self.cli.sunionstore(*keys)

    def sinter(self, *keys):
        return self.cli.sinterstore(*keys)

    def sdiff(self, *keys):
        return self.cli.sdifstoref(*keys)

    def hset(self, key, *kwargs):
        pass

    def hget(self):
        pass

    def hmset(self, key, *kwargs):
        pass

    def hmget(self):
        pass

    def hlen(self, key):
        self.cli.hlen(key)

    def get_keys(self, key):
        return self.cli.hkeys(key)
    def get_values(self, key):
        return self.cli.hvals(key)
    def get_keyvalues_by_dict(self, key):
        dict = {}
        for index, kv in enumerate(hgetall(key)):
            if index % 2 == 0:
                #keyに入れる
                pass
            else:
                #valueに入れる
                pass
        return dict

    def get_type(self, key):
        return self.cli.type(key)

    def sort_list_desc(self, key):
        return self.cli.sort(key, 'desc')

    def sort_list_ask(self, key):
        return self.cli.sort(key)

    def sort_stringlist_ask(self, key):
        return self.cli.sort(key, 'alpha')

    def sort_stringlist_ask(self, key):
        return self.cli.sort(key, 'alpha', 'desc')

class RankingRedis(AbstractRedis):
    def __init__(self):
        super(RankingRedis, self).__init__()

    def add(self, key, point, name):
        self.cli.zadd(key, point, name)

    def rem(self, key):
        self.cli.zrem(key)

    def get_ranking_desc(self, key):
        return self.cli.zrevrange(key, 0, -1)

    def get_ranking_ask(self, key):
        return self.cli.zrange(key, 0, -1)

    def get_ranking_by_name(self, key, name):
        return self.zrank(key, name)

    def get_ranking_by_name_reverse(self, key, name):
        return self.zrevrank(key, name)

