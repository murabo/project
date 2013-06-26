# coding: utf-8

from AbstractRedis import AbstractRedis

class SampleRedis2(AbstractRedis):

    attributes = {
        'sample2':'sample2',
    }

    def __init__(self):
        super(SampleRedis2, self).__init__()

    def get_kvs_key(self, **kwargs):
        return '%s' % 'dummy'
