#codind:utf-8

from AbstractDisplay import MenuDisplay

class Main(object):
    def __init__(self):
        pass

    def do_display(self):
        menu_display = MenuDisplay('H')
        menu_display.display()


if __name__ == '__main__':
        main = Main()
        main.do_display()









