#coding:utf-8

from makingmodules.rediscore.RedisApi import RedisApi

class Subject(object):
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class SendMailSubject(Subject):
    def __init__(self):
        super(SendMailSubject, self).__init__()
        self.key = 'key'
        self.redisapi = RedisAPI()

    def register(self, observer):
        user_list = self.redisapi.get_list()
        user_list.remove(observer)
        self.redisapi.delete(self.key)
        self.redisapi.append(self.key, user_list)



