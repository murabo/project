#encoding:utf8

from comparator.AgeComparator import AgeComparator
from comparator.HeightComparator import HeightComparator
from human import Human
from myclass import MyClass

class Main:
    def __init__(self):
        self.h1 = Human('hashimoto',178,83,24)
        self.h2 = Human('murakami',150,100,40)
        
        comparator = MyClass(AgeComparator()) 
        result = comparator.perform_compare(self.h1, self.h2)
        print result
        
        comparator.set_comparator(HeightComparator())
        result = comparator.perform_compare(self.h1, self.h2)
        print result
        
        # なぜこっちじゃ駄目なのか、ちゃんと考える
        result = AgeComparator().compare(self.h1, self.h2)
        print result

        result = HeightComparator().compare(self.h1, self.h2)
        print result












