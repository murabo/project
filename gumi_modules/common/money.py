# -*- coding: utf-8 -*-
from __future__ import absolute_import

from common.static_values import StaticValues
from common.image import ImageMixin


class Money(ImageMixin):

    def __init__(self, number):
        self.id = 'money'
        self.img_folder = 'point'
        self.number = number
        self.type = StaticValues.TYPE_MONEY

    def __unicode__(self):
        return u'%d銭' % self.number

    @property
    def name(self):
        return u'%d銭' % (self.number)
