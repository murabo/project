# coding: utf-8

import gredis


class RedisMixin(object):
    redis_name = ''

    @property
    def redis(self):
        if hasattr(self, '_redis'):
            return self._redis
        self._redis = gredis.get(self.redis_name)
        return self._redis
