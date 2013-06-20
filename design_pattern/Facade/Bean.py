#coding:utf-8

class Bean:
    def __init__(self): raise Exception("Do not construct instances")

    @classmethod
    def getProperties(cls):
        return [
                 ("hyuki@hyuki.com", "Hiroshi Yuki")
               , ("hanako@hyuki.com", "Hanako Sato")
               , ("tomura@hyuki.com", "Tomura")
               , ("mamoru@hyuki.com", "Mamoru Takahashi")
               ]

