#coding:utf-8

from IDCard import IDCardFactory
class Main:
    def __init__(self):
        factory = IDCardFactory()
        card1 = factory.create(u"はしもと")
        card2 = factory.create(u"しらかわ")
        card1.use()
        card2.use()

if __name__ == '__main__':
    main = Main()
