#coding:utf-8

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

