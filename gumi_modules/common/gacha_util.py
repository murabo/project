# -*- coding: utf-8 -*-

class GachaUtil(object):
    """
    ガチャ用のUtilクラス
    """

    def __init__(self):
        pass

    @classmethod
    def category_and_rarity_sort(cls, x, y):
        """
        レアリティ高い順にソート
        カテゴリ別にはソートしない
        """
        return int(y.rarity - x.rarity)