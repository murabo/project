# -*- coding: utf-8 -*-

import time
import logging

import msgpack
from kvs.generic import KVS

from tokyotyrant import tt_operator

from opensocial.models import OpenSocialUser, get_osuser
from gokudo.player.models import Player

class TokyoTyrantStorage(object):
    """
    TokyoTyrantをディクショナリとして使う基底クラス
    継承して使ってください
    """
    
    KVS_KEY_FORMAT = u'TokyoTyrantStorage::%s' #上書きすること
    
    player  = None
    osuser  = None
    user_id = None
    kvs_key = None
    
    storage = {}
    
    def __init__(self, player):
        if isinstance(player, Player):
            self.player  = player
            self.user_id = player.osuser.userid
        else:
            self.user_id = str(player)
        
        self.kvs_key = self.KVS_KEY_FORMAT % self.user_id
        
        #TTから取得
        try:
            bulk_strage = tt_operator.getobj(self.kvs_key)
        except ValueError:
            self.save()
            return
        if bulk_strage:
            self.storage = bulk_strage
        else:
            #TTにレコードが無いのでデフォルトをセーブ
            self.save()
    
    def save(self):
        """
        storageを保存
        """
        self.storage['updated_at'] = int(time.time())
        tt_operator.setobj(self.kvs_key, self.storage)
    
    def delete(self):
        """
        完全削除
        """
        tt_operator.out(self.kvs_key)
        
    
    def dump(self):
        logging.debug("TokyoTyrantStorage: debug: %s" % self.storage)
    
    def get(self, k, default=None):
        return self.storage.get(k,default)
    
    def set(self, k, value):
        self.storage[k] = value
    
    def get_osuser(self):
        '''
        osuserインスタンスが無かったら作って返す
        ※本クラスのコンストラクタで、osuserを文字列で渡すと self.osuser が Noneのまま
        インスタンス化される。その場合でもosuserがほしい時用。
        '''
        if self.osuser is None:
            self.osuser = get_osuser(self.user_id)
        return self.osuser


class MessagePackKVS(object):
    '''
    msgpackを簡単に扱う
    '''
    def __init__(self, *args, **argv):
        self.kvs = KVS(kvsclass='TTStr', *args, **argv)

    def get(self, default=None, keyvalue=None):
        value = self.kvs.get(keyvalue=keyvalue)
        if value is None:
            return default
        else:
            return msgpack.unpackb(value)
    
    def set(self, value, keyvalue=None):
        self.kvs.set(msgpack.packb(value), keyvalue=keyvalue)

    def delete(self, keyvalue=None):
        self.kvs.delete(keyvalue=keyvalue)
