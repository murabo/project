#coding:utf-8

from HtmlWriter import HtmlWriter
from Database import Database

class PageMaker(object):
    def __init__(self): raise Exception("Do not construct instances")

    @classmethod
    def makeLinkPage(cls,  filename):
        try:
            fsock = open(filename, 'w')
        except IOError,  (errno, strerror):
            print "I/O error(%s): %s" % (errno, strerror)

        htmlwriter = HtmlWriter(fsock)
        dbList = Database.getProperties()

        htmlwriter.makeTitle("Link page")
        for t in dbList:
            htmlwriter.makeMailTo(t[0],  t[1])
        htmlwriter.close()



