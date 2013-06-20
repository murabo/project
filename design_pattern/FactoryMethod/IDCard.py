#coding:utf-8

from Factory import Factory, Product

class IDCardFactory(Factory):
    def __init__(self): self.owners = []
    def createProduct(self, owner):
        idcard = IDCard(owner)
        return idcard
    def registerProduct(self,  product): self.owners.append(product)

class IDCard(Product):
    def __init__(self, owner): self.owner = owner
    def use(self): print self.owner+u"が使っています"


