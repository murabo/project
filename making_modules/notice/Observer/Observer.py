#coding:utf-8

class Observer(object):
    def __init__(self, user_id, subject):
        self.user_id = user_id
        subject.register(self)
        
    def update(self):
         raise NotImplementedError

class SendMailObserver(Observer):
    def __init__(self, *args):
        Observer.__init__(self, *args)
        
    def update(self):
        print 'SendMail'





