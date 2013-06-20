# -*- coding: utf-8 -*-
import datetime
import time
import pickle
from django.conf import settings


class DatetimeUtil(object):
    '''
    日付時刻のユーティリティクラス
    '''

    @classmethod
    def now(cls):
        """
        現在時刻を返すラッパー関数
        ※settingsで設定されていればそちらを優先する
        """
        if settings.DEBUG and cls.get_debug_timestamp():
            return datetime.datetime.fromtimestamp(cls.get_debug_timestamp())
        if settings.DEBUG and cls.get_debug_timeoffset():
            d, h = cls.get_debug_timeoffset()
            if cls.get_debug_offsetdirection():
                return datetime.datetime.now() - datetime.timedelta(hours=h, days=d)
            return datetime.datetime.now() + datetime.timedelta(hours=h, days=d)
        if not hasattr(settings, 'DATETIME_SETTING') or settings.DATETIME_SETTING is None:
            return datetime.datetime.now()
        else:
            return settings.DATETIME_SETTING


    @classmethod
    def is_exceeded_date(cls, offset_hour, last_datetime):
        """
        日付が切り替わっているか見る。

        offset_hour:切り替え時間(0-23)
        last_datetime:最終時刻(datetiem型)
        """
        offset_time_delta = datetime.timedelta(hours=offset_hour)
        now_offset = datetime.datetime.now() - offset_time_delta
        last_offset = last_datetime - offset_time_delta
        ex_time_delta = now_offset.date() - last_offset.date()
        return ex_time_delta.days > 0


    @classmethod
    def get_exceeded_date(cls, offset_hour):
        """
        日付が切り替わる時間を取得

        offset_hour:切り替え時間(0-23)
        """
        d = cls.now()
        ex_date = None
        if d.hour < offset_hour:
            ex_date = (d - datetime.timedelta(days=1))
        else:
            ex_date = d

        return datetime.datetime(ex_date.year, ex_date.month, ex_date.day, offset_hour)


    @classmethod
    def str_to_timestamp(cls, datetime_str):
        '文字列日時をタイムスタンプに変換する'
        d = datetime.datetime(*time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")[0:6])
        return time.mktime(d.timetuple())


    @classmethod
    def str_to_datetime(cls, datetime_str):
        '文字列日時をdatetimeオブジェクトに変換する'
        return datetime.datetime.fromtimestamp(cls.str_to_timestamp(datetime_str))


    @classmethod
    def datetime_to_timestamp(cls, datetime_obj):
        """
        タイムスタンプに変換
        """
        return time.mktime(datetime_obj.timetuple())


    @classmethod
    def days_to_seconds(cls, days):
        """
        日にちを秒に変換
        """
        return days * 24 * 60 * 60


    @classmethod
    def hours_to_seconds(cls, hour):
        """
        時間を秒に変換
        """
        return hour * 60 * 60

    @classmethod
    def _get_debug_dayoffset_key(cls):
        return 'develop:debug_dayoffset'

    @classmethod
    def _get_debug_houroffset_key(cls):
        return 'develop:debug_houroffset'

    @classmethod
    def _get_debug_offsetdirection_key(cls):
        return 'develop:debug_offsetdirection'

    @classmethod
    def set_debug_timeoffset(cls, d=0, h=0, direction=0):
        '''
        デバッグ用タイムオフセットを設定する
        '''
        from tokyotyrant import tt_money
        cls.reset_debug_timesettings()
        tt_money.putint(cls._get_debug_dayoffset_key(), d)
        tt_money.putint(cls._get_debug_houroffset_key(), h)
        tt_money.putint(cls._get_debug_offsetdirection_key(), direction)

    @classmethod
    def get_debug_timeoffset(cls):
        '''
        デバッグ用タイムオフセットを取得する
        '''
        from tokyotyrant import tt_money
        d = tt_money.getint(cls._get_debug_dayoffset_key())
        h = tt_money.getint(cls._get_debug_houroffset_key())
        if d or h:
            return d, h
        return None

    @classmethod
    def get_debug_offsetdirection(cls):
        '''
        デバッグ用オフセット方向を取得する
        '''
        from tokyotyrant import tt_money
        return tt_money.getint(cls._get_debug_offsetdirection_key())

    @classmethod
    def _get_debug_timestamp_key(cls):
        return 'develop:debug_timestamp'

    @classmethod
    def set_debug_timestamp(cls, timestamp):
        '''
        デバッグ用タイムスタンプを設定する
        '''
        from tokyotyrant import tt_money
        cls.reset_debug_timesettings()
        tt_money.putint(cls._get_debug_timestamp_key(), timestamp)

    @classmethod
    def set_debug_timestamp_by_ymdhis(cls, y, m, d, h=0, i=0, s=0):
        '''
        デバッグ用タイムスタンプを年月日時分秒で設定する
        '''
        timestamp = int(time.mktime(datetime.datetime(y, m, d, h, i, s).timetuple()))
        cls.set_debug_timestamp(timestamp)

    @classmethod
    def get_debug_timestamp(cls):
        '''
        デバッグ用タイムスタンプを取得する
        '''
        from tokyotyrant import tt_money
        return tt_money.getint(cls._get_debug_timestamp_key())

    @classmethod
    def reset_debug_timesettings(cls):
        '''
        デバッグ用時刻設定を解除する
        '''
        from tokyotyrant import tt_money
        tt_money.putint(cls._get_debug_timestamp_key(), 0)
        tt_money.putint(cls._get_debug_dayoffset_key(), 0)
        tt_money.putint(cls._get_debug_houroffset_key(), 0)
