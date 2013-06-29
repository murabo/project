# coding: utf-8

from AbstractRedis import AbstractRedis

class SampleRedis(AbstractRedis):

    attributes = {
        'sample':'sample',
    }

    def __init__(self):
        super(SampleRedis, self).__init__()
        self.get_and_create_subkey()

    def get_key(self):
        return '%s' % 'dummy'

    def get_and_create_subkey(self):
        subkey_prefix = 'dummy-sub1'
        self.subkey1 = self.create_subkey(subkey_prefix)
        subkey_prefix = 'dummy-sub2'
        self.subkey2 = self.create_subkey(subkey_prefix)

