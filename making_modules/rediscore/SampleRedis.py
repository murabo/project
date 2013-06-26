# coding: utf-8

from AbstractRedis import AbstractRedis

class SampleRedis(AbstractRedis):

    attributes = {
        'sample':'sample',
    }

    def __init__(self):
        super(SampleRedis, self).__init__()

    def get_kvs_key(self, **kwargs):
        return '%s' % 'dummy'
