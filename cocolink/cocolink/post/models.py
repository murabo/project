# -*- coding: utf-8 -*-
from django.db import models
from cocolink.category.models import CategoryMiddle
from cocolink.myuser.models import MyUser
class Post(models.Model):
    u"""
    投稿情報
    """
    user    = models.ForeignKey(MyUser, verbose_name=u'ユーザ', db_index=True)
    body_text  = models.TextField(verbose_name=u"コメント本文", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    lat_x = models.TextField(verbose_name=u"座標X", max_length=30)
    lng_y = models.TextField(verbose_name=u"座標Y", max_length=30)
    value = models.IntegerField()
    reference = models.TextField(verbose_name=u"座標X", max_length=30)
    category = models.ForeignKey(CategoryMiddle, verbose_name=u'中カテゴリ', db_index=True)

    class Meta:
        verbose_name = u'投稿情報'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'ID:%s | UserID:%s ' % (self.id, self.user_id)