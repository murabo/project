#coding:utf-8

class Shop(object):
    def __init__(self):
        self.shop_search = None

    def perform_get_shop(self):
        print 'オブジェクトチェック：%s' % self.shop_search 
        return self.shop_search.get_shop()

    def set_shop(self, shop_search):
        self.shop_serach = shop_search

class RecommendShop(Shop):
    def __init__(self):
        #super(RecocomendShop, self).__init__()
        Shop.__init__(self) 
        self.set_shop(RecommendShopSearch())

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
        return 1

class Main:
    def __init__(self):
        obj = RecommendShop()
        shop = obj.perform_get_shop()

if __name__ == '__main__':
        main = Main()
