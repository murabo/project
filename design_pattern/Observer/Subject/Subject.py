#coding:utf-8

class Subject:
    def __init__(self, event):
        self.observers = []
        self.event = event
    def register(self, listener):
        self.observers.append(listener)
    def unregister(self, listener):
        self.remove(listener)
    def notify_observers(self,event):
        for observer in self.observers:
            observer.update(event)