#coding:utf-8

class Shop(object):
    def __init__(self):
        self.shop_search = None

    def perform_get_shop(self):
        return self.shop.get_shop(self)

    def _set_shop(self, shop_search):
        self.shop_serach = shop_search

class RecommendShop(Shop):
    def __init__(self):
       # super(RecommendationShop, self).__init__():
        self._set_shop(RecommendShopSearch())

class ShopSearch(object):
    def __init__(self):
        pass

class TopShopSearch(ShopSearch):
    def __init__(self):
        pass

class RecommendShopSearch(ShopSearch):
    def __init__(self):
        pass

    def get_shop(self):
        pass

class Main:
    def __init__(self):
        obj = RecommendationShop()
        shop = obj.perform_get_shop()

