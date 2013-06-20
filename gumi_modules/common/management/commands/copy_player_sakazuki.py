# -*- coding: utf-8 -*-

"""
プレイヤーの盃ポイントを別のTTサーバーに移す
"""

from django.core.management.base import BaseCommand
from player.models import Player

DEBUG_EXECUTE_NUM = 100

class Command(BaseCommand):
    def handle(self, *args, **options):
        # デバッグモード
        debug = True
        if len(args) == 1:
            if args[0] == 'execute':
                debug = False

        for i, player in enumerate(Player.objects.all()):
            if i >= DEBUG_EXECUTE_NUM and debug:
                print 'debug finished.'
                return

            # 盃ポイント
            old_value = old_getter(player)
            new_setter(player, old_value)
            new_value = new_getter(player)
            print 'Player:%s old:%s -> new:%s' % (player.pk, old_value, new_value)
            if old_value != new_value:
                print 'verify error'
                return

            # 被盃ポイント
            old_value = old_getter2(player)
            new_setter2(player, old_value)
            new_value = new_getter2(player)
            print 'Player:%s old:%s -> new:%s' % (player.pk, old_value, new_value)
            if old_value != new_value:
                print 'verify error'
                return

        print 'finished.'

'''
移したいTTのgetter, setter
'''
def old_getter(player):
    return player.get_current_communication_point_old()

def new_getter(player):
    return player.get_current_communication_point()

def new_setter(player, value):
    player.set_communication_point(value)


def old_getter2(player):
    return player.get_receive_communication_point_old()

def new_getter2(player):
    return player.get_receive_communication_point()

def new_setter2(player, value):
    player.set_receive_communication_point(value)
