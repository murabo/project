#coding:utf-8

class Factory:
    def __init__(self): raise Exception ("abstract class")
    def createProduct(self, owner): raise NotImplementedError
    def registerProduct(self, product): raise NotImplementedError
    def create(self, owner):
        product = self.createProduct(owner)
        self.registerProduct(product)
        return product

class Product:
    def __init__(self): raise Exception("abstract class")
    def use(self): raise NotImplementedError

