# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models
from common.datetime_util import DatetimeUtil


class PeriodMixin(models.Model):
    begin_at = models.DateTimeField(u'開始日時', blank=True, null=True, default=None)
    end_at = models.DateTimeField(u'終了日時', blank=True, null=True, default=None)

    class Meta:
        abstract = True

    def in_period(self):
        now = DatetimeUtil.now()
        if self.begin_at and now < self.begin_at:
            return False
        if self.end_at and self.end_at <= now:
            return False
        return True
