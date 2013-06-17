# -*- coding: utf-8 -*-
import struct
import time
from threading import local
import pytyrant

import logging
import sys
import errno
import socket

from django.conf import settings
from django.core import signals
from django.utils.encoding import smart_unicode, smart_str
from django.utils import simplejson

RDBMONOULOG = pytyrant.RDBMONOULOG
RDBXOLCKREC = pytyrant.RDBXOLCKREC
RDBXOLCKGLB = pytyrant.RDBXOLCKGLB

__all__ = ['RDBMONOULOG', 'RDBXOLCKREC', 'RDBXOLCKGLB']

######

DEFAULT_PORT = 1978

class TT(local):
    def __init__(self, host='127.0.0.1', port=DEFAULT_PORT, shost=None, sport=DEFAULT_PORT):
        self._host = host
        self._port = port
        self._shost = shost
        self._sport = sport
        self._client = None
        self.connect()

    def connect(self):
        try:
            self._client = pytyrant.Tyrant.open(self._host, self._port)
        except socket.error, e:
            (errcode, message) = e
            if self._shost is not None:
                # if standby host is set try connect to it
                if errcode == errno.ECONNREFUSED:
                    # 'Connection refused'
                    self._client = pytyrant.Tyrant.open(self._shost, self._sport)
                else:
                    logging.error(errcode)
                    logging.error(message)
                    logging.error(self._host + ':' +str(self._port))
                    raise
            else:
                logging.error(errcode)
                logging.error(message)
                logging.error(self._host + ':' +str(self._port))
                raise

    def close(self):
        pass
#         if self._client is not None:
#             try:
#                 try:
#                     self._client.close()
#                 except:
#                     ## TODO
#                     raise
#             finally:
#                 self._client = None

    def get(self, key, default=None):
        """
        >>> tt = TT()
        >>> tt.put('get_key', 'get_value')
        >>> tt.get('get_key')
        'get_value'
        """
        try:
            return self._client.get(key)
        except pytyrant.TyrantError, e:
            return default
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            try:
                return self._client.get(key)
            except pytyrant.TyrantError, e:
                return default

    def put(self, key, value):
        """
        >>> tt = TT()
        >>> tt.put('put_key', 'put_value')
        >>> tt.get('put_key')
        'put_value'
        """
        try:
            return self._client.put(key, value)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.put(key, value)

    def putkeep(self, key, value):
        """
        Set key to value if key doesn't already exist
        """
        try:
            self._client.putkeep(key, value)
            return True
        except pytyrant.TyrantError, e:
            return False
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            try:
                self._client.putkeep(key, value)
                return True
            except pytyrant.TyrantError, e:
                return False

    def putcat(self, key, value):
        """
        Append value to the existing value for key, or set key to
        value if it does not already exist
        """
        try:
            return self._client.putcat(key, value)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.putcat(key, value)

    def putshl(self, key, value, width):
        try:
            return self._client.putshl(key, value, width)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.putshl(key, value, width)


    def putnr(self, key, value):
        """
        Set key to value without waiting for a server response
        """
        try:
            return self._client.putnr(key, value)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.putnr(key, value)

    def out(self, key):
        """
        >>> tt = TT()
        >>> tt.put("outkey", "outvalue")
        >>> tt.out("outkey")
        """
        try:
            return self._client.out(key)
        except pytyrant.TyrantError, e:
            return False
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            try:
                return self._client.out(key)
            except pytyrant.TyrantError, e:
                return False

    def mget(self, keys):
        try:
            return self._client.mget(keys)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.mget(keys)

    def iterinit(self):
        try:
            return self._client.iterinit()
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.iterinit()

    def iternext(self):
        try:
            return self._client.iternext()
        except pytyrant.TyrantError, e:
            ## TODO
            return None
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            try:
                return self._client.iternext()
            except pytyrant.TyrantError, e:
                ## TODO
                return None

    def fwmkeys(self, prefix, maxkeys=-1):
        try:
            return self._client.fwmkeys(prefix, maxkeys)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.fwmkeys(prefix, maxkeys)

    def addint(self, key, num=1):
        ## TODO
        ## addint is only suppported by the trunk version of pytyrant
        try:
            pytyrant.socksend(self._client.sock,
                              pytyrant._t1M(pytyrant.C.addint, key, num))
            pytyrant.socksuccess(self._client.sock)
            return pytyrant.socklen(self._client.sock)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            pytyrant.socksend(self._client.sock,
                              pytyrant._t1M(pytyrant.C.addint, key, num))
            pytyrant.socksuccess(self._client.sock)
            return pytyrant.socklen(self._client.sock)

    def stat(self):
        try:
            return self._client.stat()
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.stat()

    def misc(self, func, opts, args):
        try:
            return self._client.misc(func, opts, args)
        except socket.error, e:
            # socketエラーだったら再接続を試みる
            self.connect()
            return self._client.misc(func, opts, args)

#########

class TokyoTyrantClient(TT):
    def set(self, key, value):
        return self.put(key,value)

    def close(self, **kwds):
        super(TokyoTyrantClient, self).close()

    def putint(self, key, value):
        if not isinstance(value, (int, long)):
            raise TypeError("int or long argument required")
        return self.put(key, struct.pack('I', value))

    def putintnr(self, key, value):
        if not isinstance(value, (int, long)):
            raise TypeError("int or long argument required")
        return self.putnr(key, struct.pack('I', value))

    def pututcnow(self, key):
        return self.putintnr(key, int(time.time()))

    def getint(self, key, default=None):
        result = self.get(key, default)
        if result:
            return struct.unpack('I', result)[0]
        elif result == default:
            return default
        else:
            return 0

    # TODO そのうちなんとかする
    def getint2(self, key, default=None):
        result = self.get(key, default)
        if result == default:
            return default
        elif result:
            return struct.unpack('I', result)[0]
        else:
            return 0

    def getint_multi(self, keys):
        values = self.mget(keys)
        res = {}
        for k, v in values:
            res[k] = struct.unpack('I', v)[0]
        return res

    def _serialize(self, data):
        if isinstance(data, unicode):
            data = data.encode('utf-8')
        return simplejson.dumps(data, ensure_ascii=False).encode('utf-8')

    def _deserialize(self, data):
        value = simplejson.loads(data) 
        if isinstance(value, basestring):
            return smart_unicode(value)
        else:
            return value

    def setobj(self, key, value):
        """
        jsonでdumpできるオブジェクトをセットする
        """
        self.set(key, self._serialize(value))

    def getobj(self, key, default=None):
        """
        setobjしたオブジェクトをゲットする
        """
        value = self.get(key, None)
        if value is None:
            return default
        else:
            return self._deserialize(value)

    def get_list(self, key):
        val = self.get(smart_str(key))
        if val is None:
            return []
        else:
            return self._deserialize(val)

    def append_to_list(self, key, value, max=100):
        """
        add given value to list
        if list is not defined empty list is created
        """
        list = self.get_list(smart_str(key))
        list.append(value)
        while len(list) > max:
            list.pop(0)
        self.set(key, self._serialize(list))

    def set_list(self, key, list, max=100):
        while len(list) > max:
            list.pop()
        self.set(key, self._serialize(list))

    def remove_from_list(self, key, value):
        list_base = self.get_list(key)
        list_base.remove(value)
        self.set_list(key, list_base)
