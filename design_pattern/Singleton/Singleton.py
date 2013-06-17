#coding:utf-8

class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=object.__new__(cls, *args, **kwargs)
        return cls._instance

