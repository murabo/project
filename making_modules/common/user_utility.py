# -*- coding: utf-8 -*-

from __future__ import absolute_import
from django.core.cache import cache
import logging
from tokyotyrant import tt_operator

import datetime

from player.models import Player


from opensocial.utils.authdevice.api import get_auth_device_api


def initialize_user(osuser):
    '''
    プレイヤーを初期化する手続き
    '''
    #logging.debug("initialize_user start.", osuser)

    # ===========================================================
    # Player
    # -----------------------------------------------------------
    player = Player.get(osuser.userid)
    if player:
        tt_operator.put(player.get_prof_comment_key(), '')
        player.delete()

    # ===========================================================
    # cache clear
    # -----------------------------------------------------------
    cache.clear()
    
    # ===========================================================
    # opensocial
    # -----------------------------------------------------------
    osuser.updated_at = datetime.datetime.now() - datetime.timedelta(days=1)
    

    #logging.debug("initialize_user end.", osuser)
    
def get_and_update_auth(request, user_id):
    """
    端末が認証済みかどうかを返す。認証されていない場合、一回check_auth_device()を行って念のための更新を行う。
    """
    authdevice = get_auth_device_api(request, user_id=user_id)
    # 認証済みか
    if authdevice.is_auth_device:
        return True
    else:
        return authdevice.check_auth_device()
