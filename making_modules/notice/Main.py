#coding:utf8

from Subject.Subject import SendMailSubject
from Observer.Observer import SendMailObserver

class Main:
    def __init__(self):
        subject = SendMailSubject()
        observerA = SendMailObserver(16894, subject)
        subject.notify_observers()


if __name__ == '__main__':
        main = Main()

