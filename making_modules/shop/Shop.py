#coding:utf-8

from ShopSearch import RecommendShopSearch 

class Shop(object):
    def __init__(self):
        self.shop_search = None

    def perform_get_shop(self):
        return  self.shop_search.get_shop()

    def set_shop(self, shop_search):
        self.shop_search = shop_search

class RecommendShop(Shop):
    def __init__(self):
        #super(RecocomendShop, self).__init__()
        Shop.__init__(self) 
        self.set_shop(RecommendShopSearch())

class Main:
    def __init__(self):
        obj = RecommendShop()
        shop = obj.perform_get_shop()
        print shop

if __name__ == '__main__':
        main = Main()
