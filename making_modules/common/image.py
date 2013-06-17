# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.core.cache import cache
from django.conf import settings
import logging


class ImageMixin(object):

    @property
    def image(self):
        img_path = settings.MEDIA_URL + '/images/%s/%s/%s.gif'
        return {
            40: img_path % (self.img_folder, 40, self.id),
            70: img_path % (self.img_folder, 70, self.id),
            90: img_path % (self.img_folder, 90, self.id),
            140: img_path % (self.img_folder, 140, self.id),
        }

    @property
    def media(self, size=40):
        img_path = settings.MEDIA_ROOT + '/images/%s/%s/%s.gif' % (
            self.img_folder,
            size,
            self.id
        )
        try:
            binary = open(img_path).read()
        except IOError, (errno, msg):
            logging.error(
                'IOError errno: [%d] msg: [%s] path' % (
                    errno, msg, img_path
                )
            )
            return None
        return binary

    def image_url_s(self):
        return self.image[70]

    def image_url_mini(self):
        return self.image[40]

    @property
    def media_using_cache(self, size=40):
        cache_key = 'ImageCache:%s:%s:%s' % (self.img_folder, size, self,id)
        binary = cache.get(cache_key, None)
        if not binary:
            binary = self.media(size)
            if binary:
                cache.set(binary)
        return binary

