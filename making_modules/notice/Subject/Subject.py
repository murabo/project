#coding:utf-8

class Subject(object):
    def __init__(self, category):
        self.observers = self.get_observers(category)

    def register(self, listener):
        self.observers.append(listener)
   
    def unregister(self, listener):
        self.remove(listener)
   
    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def get_observers(self, category):
        observers = []
       # observers = cache.get()
       # if observers == None:
       #     filter
        return observers

    def set_observers(self, category):
       # cache.set
       # insert
       pass
