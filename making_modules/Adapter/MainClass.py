#coding:utf-8

class MainClass(object):
    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        print '(%s)' % self.string

    def show_with_aster(self):
        print '*%s*' % self.string

