#coding:utf-8

class HtmlWriter(object):
    def __init__(self, fsock):
        self.__fsock = fsock

    def __print(self,  string):
        try:
            print >>self.__fsock, string
        except:
            print "I/O error (%s) : %S" % (errno, strerror)

    def makeTitle(self, title):
        self.__print("<html><head><title>"+title.encode("utf-8")+"</title></head></html><body>")
        self.__print("<h1>"+title.encode("utf-8")+"</h1>")

    def makeParagraph(self, string):
        self.__print("<p>"+string.encode("utf-8")+"</p>")

    def makeLink(self,  href, caption):
        self.makeParagraph('<a href="%s">%s</a>' % (href, caption))

    def makeMailTo(self, mailaddr, username):
        self.makeLink('mailto:'+mailaddr, username)

    def close(self):
        self.__print("</body></html>")
        self.__fsock.close()

