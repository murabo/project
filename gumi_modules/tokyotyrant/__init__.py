# -*- coding: utf-8 -*-
from django.conf import settings
from django.core import signals

from tokyotyrant.tyrant import TokyoTyrantClient

client_pool = {}

class TyrantClientDoesNotDefinedError(Exception):
    pass

def get_client(tyrant_name="default"):
    
    if tyrant_name in client_pool:
        return client_pool[tyrant_name]
    
    if not tyrant_name in settings.TYRANT_DATABASES:
        raise TyrantClientDoesNotDefinedError()
    
    opts = {
        'host' : settings.TYRANT_DATABASES[tyrant_name]['HOST'],
        'port' : int(settings.TYRANT_DATABASES[tyrant_name]['PORT']),
    }

    if 'SHOST' in settings.TYRANT_DATABASES[tyrant_name]:
        opts['shost'] = settings.TYRANT_DATABASES[tyrant_name]['SHOST']
    if 'SPORT' in settings.TYRANT_DATABASES[tyrant_name]:
        opts['sport'] = int(settings.TYRANT_DATABASES[tyrant_name]['SPORT'])

    client = TokyoTyrantClient(**opts)
    client_pool[tyrant_name] = client
    signals.request_finished.connect(client.close)
    return client

def get_client_legacy(**opts):
    # 同一ホスト、ポートへの接続は使いまわす
    pool_key = (opts["host"],opts["port"])
    if pool_key in client_pool:
        return client_pool[pool_key]
    else:
        client = TokyoTyrantClient(**opts)
        client_pool[pool_key] = client
        signals.request_finished.connect(client.close)
        return client

if settings.ENABLE_KVS and settings.TT_OPERATOR_SERVER:
    tt_operator = get_client_legacy(**settings.TT_OPERATOR_SERVER)
else:
    tt_operator = None

if settings.ENABLE_KVS and settings.TT_ACTIVITY_SERVER:
    tt_activity = get_client_legacy(**settings.TT_ACTIVITY_SERVER)
else:
    tt_activity = None

if settings.ENABLE_KVS and settings.TT_BATTLE_SERVER:
    tt_battle = get_client_legacy(**settings.TT_BATTLE_SERVER)
else:
    tt_battle = None

if settings.ENABLE_KVS and settings.TT_ITEM_SERVER:
    tt_item = get_client_legacy(**settings.TT_ITEM_SERVER)
else:
    tt_item = None

if settings.ENABLE_KVS and settings.TT_INQUIRY_SERVER:
    tt_inquiry = get_client_legacy(**settings.TT_INQUIRY_SERVER)
else:
    tt_inquiry = None

if settings.ENABLE_KVS and settings.TT_RANKING_SERVER:
    tt_ranking = get_client_legacy(**settings.TT_RANKING_SERVER)
else:
    tt_ranking = None
    
if settings.ENABLE_KVS and settings.TT_KACHIKOMI_SERVER:
    tt_kachikomi = get_client_legacy(**settings.TT_KACHIKOMI_SERVER)
else:
    tt_kachikomi = None

if settings.ENABLE_KVS and settings.TT_EVENT_SERVER:
    tt_event = get_client_legacy(**settings.TT_EVENT_SERVER)
else:
    tt_event = None

if settings.ENABLE_KVS and settings.TT_EVENT_ZWEI_SERVER:
    tt_event2 = get_client_legacy(**settings.TT_EVENT_ZWEI_SERVER)
else:
    tt_event2 = None

if settings.ENABLE_KVS and settings.TT_POWER_SERVER:
    tt_power = get_client_legacy(**settings.TT_POWER_SERVER)
else:
    tt_power = None

if settings.ENABLE_KVS and settings.TT_MONEY_SERVER:
    tt_money = get_client_legacy(**settings.TT_MONEY_SERVER)
else:
    tt_money = None

if settings.ENABLE_KVS and settings.TT_SAKAZUKI_SERVER:
    tt_sakazuki = get_client_legacy(**settings.TT_SAKAZUKI_SERVER)
else:
    tt_sakazuki = None

if settings.ENABLE_KVS and settings.TT_POKE_SERVER:
    tt_poke = get_client_legacy(**settings.TT_POKE_SERVER)
else:
    tt_poke = None
