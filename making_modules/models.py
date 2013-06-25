# coding: utf-8

from datetime import timedelta
from eventmodules.application.gate import constants as ESV
from eventmodules.components.comp_event_place.models import EventPlace, \
    EventPlaceYakuza, EventPlaceTreasure, EventPlacePays
from eventmodules.components.comp_gate.models import PlayerStockItem
from eventmodules.components.comp_raid.models import RaidBattle
from gredis.attribute import AttributeRedis
from module.wrapper.entity import get_entity
from module.wrapper.gift import gift_official_presents
from yakuza.models import Yakuza
import datetime
import random



class PlayerPlace(AttributeRedis):

    attributes = {
    }

    def __init__(self, event, player):
        super(PlayerPlace, self).__init__(player=player, event=event)
        self.player = player
        self.event = event

    def get_kvs_key(self, **kwargs):
        player = kwargs.get('player', None)
        event = kwargs.get('event', None)
