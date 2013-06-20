# coding: utf-8

from common.static_values import StaticValues
from yakuza.models import Yakuza, PlayerYakuza
from item.models import GameItem
from gokujo.models import Gokujo
from present.models import PlayerPresent
from common.money import Money
from common.point_entity import Point
from common.medal import Medal
from common.actionlog_utils import ActionLogUtils
from equipment.models import (
    GokujoEquipmentItem,
    YakuzaEquipmentItem
)


def get_player_presents(player, entity, msg, time_limited=None):
    entity, quantity = entity
    presents = []
    entity_type = StaticValues.TYPE_NONE
    if isinstance(entity, Yakuza):
        entity_type = StaticValues.TYPE_CARD
        for i in range(quantity):
            player_yakuza = PlayerYakuza.create(player=None, yakuza=entity)
            presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_CARD, present=player_yakuza.pk, num=1, text=msg))
    elif isinstance(entity, PlayerYakuza):
        entity_type = StaticValues.TYPE_CARD
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_CARD, present=entity.pk, num=1, text=msg))
    elif isinstance(entity, GameItem):
        entity_type = StaticValues.TYPE_ITEM
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_ITEM, present=entity.pk, num=quantity, text=msg))
    elif isinstance(entity, Gokujo):
        entity_type = StaticValues.TYPE_TREASURE
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_TREASURE, present=entity.pk, num=quantity, text=msg))
    elif isinstance(entity, Money):
        entity_type = StaticValues.TYPE_MONEY
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_MONEY, present=entity.number, text=msg))
    elif isinstance(entity, Point):
        entity_type = StaticValues.TYPE_POINT
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_POINT, present=entity.number, text=msg))
    elif isinstance(entity, Medal):
        entity_type = StaticValues.TYPE_POINT
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_POINT, present=entity.number, text=msg))
    elif isinstance(entity, GokujoEquipmentItem):
        entity_type = StaticValues.TYPE_GOKUJOEQUIP
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_GOKUJOEQUIP, present=entity.pk, num=quantity, text=msg))
    elif isinstance(entity, YakuzaEquipmentItem):
        entity_type = StaticValues.TYPE_YAKUZAEQUIP
        presents.append(PlayerPresent(player_id=player.pk, type=StaticValues.TYPE_YAKUZAEQUIP, present=entity.pk, num=quantity, text=msg))
    ActionLogUtils.write_give_official_present_log(player, entity, msg, entity_type, quantity)
    return presents 


def gift_official_present(player, entity, msg, time_limited=None):
    presents = get_player_presents(player, entity, msg, time_limited=None)

    return PlayerPresent.objects.bulk_create(presents)


def gift_official_presents(player, entities, time_limited=None):
    """
    params: player <class: Player>
    params: entities <tuple: entity, quantity <int>, msg <unicode>>
    params: time_limited <datetime>
    """
    presents = []
    for entity, quantity, msg in entities:
        presents.extend(get_player_presents(player, (entity, quantity), msg, time_limited))

    return PlayerPresent.objects.bulk_create(presents)
