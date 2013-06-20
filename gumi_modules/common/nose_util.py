# -*- encoding: UTF-8 -*-

"""
testで使用する共通のメソッド
ファイル名にtestを使っていないのは'python manage.py test'を実行した時にテストファイルと認識されるため
"""

import datetime
from opensocial.models import OpenSocialUser
from player.models import Player
from common.static_values import StaticValues

def create_player(osuserid):
    player = Player.get(osuserid)
    if player:
        return player
    osuser, is_new  = OpenSocialUser.objects.get_or_create(userid=osuserid)
    osuser.nickname = u"プレイヤー%s" % osuserid
    osuser.birthday = datetime.datetime.now()
    osuser.created_at = datetime.datetime.now()
    osuser.updated_at = datetime.datetime.now()
    osuser.friend_userids = ''
    osuser.save()

    player = Player.objects.create(osuser=osuser)
    player.category = StaticValues.CATEGORY_FIGHTER
    return player

def create_players(osuserids):
    return [create_player(osuserid) for osuserid in osuserids]
