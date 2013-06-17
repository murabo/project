#coding:utf-8

from Singleton import Singleton

class Main:
    def __init__(self):
        obj1 = Singleton()
        obj2 = Singleton()

        obj1.name = 'test1'
        obj2.name = 'test2'

        print obj1.name
        print obj2.name

if __name__ == '__main__':
        main = Main()




