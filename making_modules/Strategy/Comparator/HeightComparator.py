#coding:utf8
from Comparator import Comparator


class HeightComparator(Comparator):  
    def compare(self, h1, h2):
        if (h1.height > h2.height):
            return 1
        elif (h1.height == h2.height):
            return 0
        else:
            return -1
        
