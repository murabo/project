#coding:utf-8

class Recommendation(object):
    def __init__(self):
        self.shop = None

    def _get_shop(self):
        return self.shop.get_shop(self)

    def _set_shop(self, shop):
        self.shop = shop

class RecommendationTop(Recommendation):
    def __init__(self):
        super(RecommendationTop, self).__init__(self):
