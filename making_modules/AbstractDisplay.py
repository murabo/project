#coding:utf-8

from abc import ABCMeta, abstractmethod

class AbstractDisplay(object):
    __metaclass__ = ABCMeta
        
    def __init__(self):
        pass
   
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def aprint(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
           self.aprint()
        self.close()
        

class MenuDisplay(AbstractDisplay):
    def __init__(self, char):
        AbstractDisplay.__init__(self)
        self.char = char

    def open(self):
        print '-----'

    def aprint(self):
        print self.char

    def close(self):
        print '-----'






