# -*- coding: utf-8 -*-
"""
django.conf.settings を直接使うと Django 依存となるので,
共通モジュールは, この gconf.Settings 経由で django.conf.settings を使用する事.

例えば, 次のようなカスタム Settings を定義する.

.. code-block:: python

    from gconf import Settings

    class EggSettings(Settings):
        default_settings = {
            'SPAM': 'ham',
        }


その後, 次のように利用する.

>>> from egg.conf import EggSettings
>>> settings = EggSettings()
>>> settings.SPAM


この場合, settings.SPAM は次のような優先順位で値を決定する.

1. django.conf.settings.SPAM
2. egg.conf.EggSettings.default_settings['SPAM']
3. raise AttributeError, 'SPAM'

django.conf.settings の import に成功していても
1. で取得できなければ 2. で取得を行うため,
デフォルト値の定義としても利用できる.
"""

class Settings(object):
    default_settings = {}

    def __init__(self, **kwargs):
        try:
            from django.conf import settings
            self._settings = settings
        except ImportError:
            self._settings = None

    def __getattr__(self, name):
        if self._settings:
            try:
                return getattr(self._settings, name)
            except ImportError:
                # Django Settings は遅延ロードであるため,
                # ここで ImportError になるパターンもある.
                self._settings = None
            except AttributeError:
                pass

        try:
            return self.default_settings[name]
        except KeyError:
            raise AttributeError, name