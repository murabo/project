# coding: utf-8
from __future__ import absolute_import, with_statement

import gredis


class BaseStockItem(object):
    def __init__(self):
        self.redis = gredis.get()

    def get(self):
        return self.redis.lrange(self.key, 0, -1)

    def set(self, value):
        if isinstance(value, list):
            with self.redis.pipeline() as pipe:
                pipe.multi()
                for v in value:
                    pipe.rpush(self.key, v)
                pipe.execute()
        else:
            return self.redis.rpush(self.key, value)

    def delete(self):
        return self.redis.delete(self.key)


class PlayerStockItem(BaseStockItem):
    def __init__(self, player_id, event_id):
        super(PlayerStockItem, self).__init__()
        self.player_id = player_id
        self.event_id = event_id

    @property
    def key(self):
        return '%s:EVENT:%sPLAYER:%s' % (
            self.__class__.__name__,
            self.event_id,
            self.player_id
        )


class BossBattleStockItem(BaseStockItem):
    def __init__(self, event_id, battle_id):
        super(BossBattleStockItem, self).__init__()
        self.event_id = event_id
        self.battle_id = battle_id

    @property
    def key(self):
        return '%s:EVENT:%s:BATTLE:%s' % (
            self.__class__.__name__,
            self.event_id,
            self.battle_id
        )
