#coding:utf-8
from Adapter import Adapter

class Main:
    def __init__(self):
        obj = Adapter('はしもと')
        obj.print_weak()
        obj.print_strong()

if __name__ == '__main__':
    main = Main()




