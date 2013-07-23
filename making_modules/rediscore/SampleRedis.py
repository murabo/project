# coding: utf-8

from AbstractRedis import AbstractRedis

class SampleRedis(AbstractRedis):

    attributes = {
        'sample':'sample',
    }

    key_prefix = 'dummy'
    subkey_prefix = {
        1 :'dummy-sub1',
        2 :'dummy-sub2',
    }

    def __init__(self):
        super(SampleRedis, self).__init__()
        self.get_and_create_subkey()

    def get_key(self):
        return '%s' % self.__class__.key_prefix

    def get_and_create_subkey(self):
        subkey_prefix1 = self.__class__.subkey_prefix[1]
        subkey_prefix2 = self.__class__.subkey_prefix[2]
        self.subkey1 = self.create_subkey(subkey_prefix1)
        self.subkey2 = self.create_subkey(subkey_prefix2)

class SampleRedis2(AbstractRedis):

    attributes = {
        'sample':'sample',
    }

    key_prefix = 'dummy2'
    subkey_prefix = {
        1 :'dummy2-sub1',
        2 :'dummy2-sub2',
    }

    def __init__(self):
        super(SampleRedis2, self).__init__()
        self.get_and_create_subkey()

    def get_key(self):
        return '%s' % self.__class__.key_prefix

    def get_and_create_subkey(self):
        subkey_prefix1 = self.__class__.subkey_prefix[1]
        subkey_prefix2 = self.__class__.subkey_prefix[2]
        self.subkey1 = self.create_subkey(subkey_prefix1)
        self.subkey2 = self.create_subkey(subkey_prefix2)
