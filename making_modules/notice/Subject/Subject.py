#coding:utf-8

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
        Subject.__init__(self)


