# -*- coding: utf-8 -*-
from __future__ import absolute_import

from common.static_values import StaticValues
from common.money import Money
from common.point_entity import Point
from common.medal import Medal
from yakuza.models import Yakuza
from item.models import GameItem
from equipment.models import YakuzaEquipmentItem

def get_entity(type, id, num):
    if type == StaticValues.TYPE_CARD:
        entity = Yakuza.get(id)
    elif type == StaticValues.TYPE_ITEM:
        entity = GameItem.get(id)
    elif type == StaticValues.TYPE_MONEY:
        entity = Money(num)
    elif type == StaticValues.TYPE_POINT:
        entity = Point(num)
    elif type == StaticValues.TYPE_MEDAL:
        entity = Medal(num)
    elif type == StaticValues.TYPE_YAKUZAEQUIP:
        entity = YakuzaEquipmentItem.get(id)

    return entity
