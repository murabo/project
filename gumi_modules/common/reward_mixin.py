# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models
from common.entity_util import get_entity


class RewardMixin(models.Model):
    reward_type = models.IntegerField(u'報酬タイプ')
    reward_id = models.IntegerField(u'報酬ID')
    reward_quantity = models.IntegerField(u'報酬個数', default=1)

    class Meta:
        verbose_name = u'報酬'
        abstract = True

    @property
    def reward(self):
        return get_entity(self.reward_type, self.reward_id, self.reward_quantity)
