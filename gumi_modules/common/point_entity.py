# -*- coding: utf-8 -*-
from __future__ import absolute_import

from common.image import ImageMixin
from common.static_values import StaticValues


class Point(ImageMixin):

    def __init__(self, number):
        self.id = 'point'
        self.img_folder = 'point'
        self.number = number
        self.type = StaticValues.TYPE_POINT

    def __unicode__(self):
        return u'%s盃pt' % self.number

    @property
    def name(self):
        return u'%s盃pt' % self.number
