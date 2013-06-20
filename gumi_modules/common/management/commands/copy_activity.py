# -*- coding: utf-8 -*-

"""
アクティビティを別のTTサーバーに移す
"""

from django.core.management.base import BaseCommand
from player.models import Player
from mobile.activity import Activity

DEBUG_EXECUTE_NUM = 1
GET_STEP = 100

class Command(BaseCommand):
    def handle(self, *args, **options):
        # デバッグモード
        debug = True
        if len(args) == 1:
            if args[0] == 'execute':
                debug = False

        i = 0
        while True:
            players = Player.objects.all()[i:i+GET_STEP]
            if not players:
                break
            for cnt, player in enumerate(players):
                if cnt >= DEBUG_EXECUTE_NUM and debug:
                    print 'debug finished.'
                    return

                # copy 1
                old_value = old_getter(player)
                new_setter(player, old_value)
                new_value = new_getter(player)
                print 'Player:%s old:%s -> new:%s' % (player.pk, old_value, new_value)
                if old_value != new_value:
                    print 'verify error'
                    return

                # copy 2
                old_value = old_getter2(player)
                new_setter2(player, old_value)
                new_value = new_getter2(player)
                print 'Player:%s old:%s -> new:%s' % (player.pk, old_value, new_value)
                if old_value != new_value:
                    print 'verify error'
                    return
            i += GET_STEP
        print 'finished.'

'''
移したいTTのgetter, setter
'''
def old_getter(player):
    return Activity.get_my_activity_old(player)

def new_getter(player):
    return Activity.get_my_activity_new(player)

def new_setter(player, value):
    Activity.set_my_activity(player, value)

def old_getter2(player):
    return Activity.get_friend_activity_old(player.pk)

def new_getter2(player):
    return Activity.get_friend_activity_new(player.pk)

def new_setter2(player, value):
    Activity.set_friend_activity(player.pk, value)
