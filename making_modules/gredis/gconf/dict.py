# -*- coding: utf-8 -*-
"""
django.conf.settings でディクショナリ型の設定を使用する際,
gconf.redis.DictSettings を使用する事.

例えば, settings.py に EGG_SETTINGS ディクショナリが定義されており,
EGG_SETTINGS 内の設定値を利用したい場合は,
次のようなカスタム Settings を定義する.

.. code-block:: python

    from gconf.dict from DictSettings

    class EggSettings(DictSettings):
        settings_name = 'EGG_SETTINGS'
        default_settings = {
            'SPAM': 'default spam',
            'HAM': 'default ham',
        }


その後, 次のように利用する.

>>> from egg.conf import EggSettings
>>> settings = EggSettings()
>>> settings.SPAM # 'default spam'
>>> settings.HAM # 'default ham'

もし, settings.py が次のように設定さいれているならば…,

.. code-block:: python

    EGG_SETTINGS = {
        'SPAM': 'spam',
    }


次のような結果が得られる.

>>> settings.SPAM # 'spam'
>>> settings.HAM # 'default ham'
"""

from gredis.gconf import Settings

class DictSettings(object):
    default_settings = {}

    def __init__(self):
        self._dict = getattr(Settings(),
                             self.settings_name,
                             self.default_settings)

    @property
    def settings_name(self):
        raise NotImplementedError

    def __getattr__(self, name):
        try:
            return self._dict[name]
        except KeyError:
            return self.default_settings[name]
