# -*- coding: utf-8 -*-
from __future__ import absolute_import

from common.static_values import StaticValues
from common.image import ImageMixin


class Medal(ImageMixin):

    def __init__(self, number):
        self.id = 'medal'
        self.img_folder = 'point'
        self.number = number
        self.type = StaticValues.TYPE_MEDAL

    def __unicode__(self):
        return u'ﾚｱ代紋'

