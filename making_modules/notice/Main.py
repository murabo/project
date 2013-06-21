#coding:utf8

from Subject.Subject import Subject
from Observer.Observer import Observer

class Main:
    def __init__(self):
        category = None
        subject = Subject(category)
        observerA = Observer(profile.pk, subject)
        subject.notify_observers()


if __name__ == '__main__':
        main = Main()

