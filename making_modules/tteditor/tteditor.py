# -*- coding: utf-8 -*-

import pytyrant
import logging
from django.conf import settings

from common.memoized_property import memoized_property #gokudoe依存

"""
TTエディタコア

"""


class TtEditor(object):
    """
    グローバル設定
    """
    
    @property
    def settings_dict(self):
        return settings.TYRANT_DATABASES


class TtEditorServer(object):
    """
    サーバ単位のオブジェクト
    """

    KEY_LIMIT = 100000

    def __init__(self, keyname_in_settings):
        """
        @param (str)keyname_in_settings settings.TYRANT_DATABASES で使っているキー名
        """
        self.name = keyname_in_settings
        self.settings = settings.TYRANT_DATABASES[keyname_in_settings]
        self.host = self.settings['HOST']
        self.port = int(self.settings['PORT'])
        logging.debug('[TTEDITOR] host=%r, port=%r' % (self.host, self.port,))

    @memoized_property
    def all_keys(self):
        """
        全キー、ただし10000件まで
        """
        return self.search_keys(search_word=None)

    def search_keys(self, search_word=None):
        tyrant = pytyrant.Tyrant.open(self.host, self.port)
        tyrant.iterinit() #いらないか
        keylist = []
        for _i in xrange(self.KEY_LIMIT):
            try:
                key = tyrant.iternext()
            except pytyrant.TyrantError: #もうキーない
                break
            if not key:
                break
            if search_word:
                if search_word in key:
                    keylist.append(key)
            else:
                keylist.append(key)
        keylist.sort()
        tyrant.close()
        return keylist


class TtEditorPackerBase(object):
    """ TTのキーをパック/アンパックするモジュール """
    
    def pack(self, value):
        """ シリアライズ """
        raise NotImplementedError()
    
    def unpack(self, value):
        """ デシリアライズ """
        raise NotImplementedError()

    def try_unpack(self, value):
        try:
            return self.unpack(value)
        except Exception, e:
            return u'[%s] %s' % (e.__class__.__name__, e.message)

class TtEditorPackerPlain(TtEditorPackerBase):
    def pack(self, value):
        return value
    def unpack(self, value):
        return value

import struct
class TtEditorPackerStruct(TtEditorPackerBase):
    def pack(self, value):
        return struct.pack('I', value)
    def unpack(self, value):
        return struct.unpack('I', value)[0]

from django.utils import simplejson
class TtEditorPackerJson(TtEditorPackerBase):
    def pack(self, value):
        return simplejson.dumps(value, ensure_ascii=False).encode('utf-8')
    def unpack(self, value):
        return simplejson.loads(value)

import cPickle as pickle
class TtEditorPackerCPickle(TtEditorPackerBase):
    def pack(self, value):
        return pickle.dumps(value)
    def unpack(self, value):
        return pickle.loads(value)

import msgpack
class TtEditorPackerMsgPack(TtEditorPackerBase):
    def pack(self, value):
        return msgpack.packb(value)
    def unpack(self, value):
        return msgpack.unpackb(value)

PACKERS = {
    'plain' : TtEditorPackerPlain,
    'struct': TtEditorPackerStruct,
    'json' : TtEditorPackerJson,
    'picle' : TtEditorPackerCPickle,
    'msgpack': TtEditorPackerMsgPack,
}

EDIT_MODES = ['msgpack', 'picle', 'plain', 'struct', 'json',]

class TtEditorKeyValue(object):
    """
    キーバリューのオブジェクト
    """
    def __init__(self, ttname, keyname, mode):
        """
        @param (str)keyname_in_settings settings.TYRANT_DATABASES で使っているキー名
        """
        self.ttname = ttname
        self.settings = settings.TYRANT_DATABASES[ttname]
        self.host = self.settings['HOST']
        self.port = int(self.settings['PORT'])
        self.keyname = keyname
        self.mode = mode
        self.packer = PACKERS[mode]()

    @memoized_property
    def _value(self):
        tyrant = pytyrant.Tyrant.open(self.host, self.port)
        v = tyrant.get(self.keyname)
        tyrant.close()
        return v

    @property
    def value(self):
        return self.packer.try_unpack(self._value)

    @property
    def repr_value(self):
        return repr(self.value)

    @property
    def native_value(self):
        return repr(self._value)

    def save(self, value):
        packed_value = self.packer.pack(value)
        tyrant = pytyrant.Tyrant.open(self.host, self.port)
        tyrant.put(self.keyname, packed_value)
        tyrant.close()

    def delete(self):
        tyrant = pytyrant.Tyrant.open(self.host, self.port)
        tyrant.out(self.keyname)
        tyrant.close()
