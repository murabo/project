#coding:utf-8

class Singleton(object)
    __obj = Singleton()
    def __init__(self):
        return self.get_instance(self)
    def get_instance(self):
        return self.__obj
