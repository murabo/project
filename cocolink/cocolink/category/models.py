# -*- coding: utf-8 -*-
from django.db import models
from cocolink.common.models import CachedMasterModel

class CategoryLarge(CachedMasterModel):
    u"""
    大カテゴリ
    """
    code  = models.TextField(verbose_name=u"カテゴリコード", blank=True, null=True, default=None)
    name = models.TextField(verbose_name=u"カテゴリ名", blank=True, null=True, default=None)

    class Meta:
        verbose_name = u'大カテゴリ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'ID:%s | Name:%s ' % (self.id, self.name)

class CategoryMiddle(CachedMasterModel):
    u"""
    中カテゴリ
    """
    l_category_id = models.ForeignKey(CategoryLarge, verbose_name=u'大カテゴリ', db_index=True)
    code  = models.TextField(verbose_name=u"カテゴリコード", blank=True, null=True, default=None)
    name = models.TextField(verbose_name=u"カテゴリ名", blank=True, null=True, default=None)

    class Meta:
        verbose_name = u'中カテゴリ'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'ID:%s | Name:%s ' % (self.id, self.name)