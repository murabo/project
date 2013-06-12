#coding:utf8

from Subject.Subject import Subject
from Observer.Observer import Observer

class Main:
    def __init__(self):
        event = None
        subject = Subject(event)
        observerA = Observer("<Observer A>", subject)
        observerB = Observer("<Observer B>", subject)
        subject.notify_observers("<event 1>")
        subject.notify_observers("<event 2>")


if __name__ == '__main__':
        main = Main()

