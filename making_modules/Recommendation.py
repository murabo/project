#coding:utf-8

class Shop(object):
    def __init__(self):
        self.shop = None

    def perform_get_shop(self):
        return self.shop.get_shop(self)

    def _set_shop(self, shop):
        self.shop = shop

class RecommendationShop(Shop):
    def __init__(self):
       # super(RecommendationShop, self).__init__():
        self._set_shop(RecommendationShopSearch())

class ShopSearch(object):
    def __init__(self):
        pass

class TopShopSearch(ShopSearch):
    def __init__(self):
        pass

class RecommendationShopSearch(ShopSearch):
    def __init__(self):
        pass

class Main:
    def __init__(self):
        obj = RecommendationShop()
        shop = obj.perform_get_shop()

