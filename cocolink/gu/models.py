# encoding:utf-8
from django.db import models
class GuPost(models.Model):
    u"""
    gu投稿情報
    """
    user_id    = models.TextField(verbose_name=u"投稿者", max_length=255)
    body_text  = models.TextField(verbose_name=u"コメント本文", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'gu投稿情報'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'ID:%s | UserID:%s ' % (self.id, self.user_id)
