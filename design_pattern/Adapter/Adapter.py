#coding:utf-8

from MainClass import MainClass

class Adapter(MainClass):
    def __init__(self, string):
       super(Adapter, self).__init__(string)
#        MainClass.__init__(string)
    def print_weak(self):
        self.show_with_paren()
    def print_strong(self):
        self.show_with_aster()

