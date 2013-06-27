# coding: utf-8

from AbstractRedis import AbstractRedis

class SampleRedis(AbstractRedis):

    attributes = {
        'sample':'sample',
    }

    def __init__(self):
        super(SampleRedis, self).__init__()

    def get_kvs_key(self):
        return '%s' % 'dummy'

    def get_new_key(self, id):
        return self.get_kvs_subkey(id)
