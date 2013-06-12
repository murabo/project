#coding:utf8
class A:
    def __init__(self):
        self.a = 1
        self.b = 2
class B(A):
    def __init__(self):
        self.c = 3
        self.d = 4
'''
上の状態だと、親クラスと子クラスでフィールドを共有してない。
b = B()
b.a
と呼びだそうとするとエラーになる。
'''        

class A:
    def __init__(self):
        self.a = 1
        self.b = 2
class B(A):
    def __init__(self):
        A.__init__(self)
        self.c = 3
        self.d = 4

'''
上のように、子クラスのinitの中で親をinitしてあげる必要がある。
b = B()
b.a
しっかりと１が帰ってくる
'''





































