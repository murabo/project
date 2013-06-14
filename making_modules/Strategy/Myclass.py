#coding:utf8

#from comparator.AgeComparator import AgeComparator

class MyClass:
    def __init__(self, comparator):
        self.comparator = comparator
    
    #@classmethod
    #def old_compare(h1, h2):
    #    return AgeComparator.compare(h1, h2)

    def perform_compare(self, h1, h2):
        return self.comparator.compare(h1, h2)
    
    def set_comparator(self, comparator):
        self.comparator = comparator


    '''
    old_compareが通常の作り
    compareがstrategyパターンを使った作り。
    
    インスタンスを渡してあげるだけ・または変えるだけで、挙動を自由に変える事ができる。
    '''
