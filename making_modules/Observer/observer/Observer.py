#coding:utf-8

class Observer:
    def __init__(self, name, subject):
        self.name = name
        self.event_list = []
        subject.register(self)
        
    def update(self, event):
        self.event_list.append (event)
        print self.name,'received event', self.event_list








