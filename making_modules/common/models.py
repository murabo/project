# -*- coding: utf-8 -*-

from django.db import models
from django.core.cache import cache
from common.memoized_property import memoized_property

class CachedMasterModel(models.Model):
    '''
    キャッシュに対応したマスターモデル
    抽象モデル
    '''
    
    class Meta:
        abstract = True
        verbose_name = u'キャッシュに対応したマスターモデル'
    
    def __unicode__(self):
        return self.name

    enable = models.BooleanField(verbose_name=u'有効', default=True)
    
    def save(self, *args, **kwargs):
        super(CachedMasterModel, self).save(*args, **kwargs)
        cache.set(self.get_cache_path(self.pk), None)
        cache.set(self.get_all_cache_path(), None)
    
    def delete(self, *args, **kwargs):
        pks = self.pk
        super(CachedMasterModel, self).delete(*args, **kwargs)
        cache.set(self.get_cache_path(pks), None)
        cache.set(self.get_all_cache_path(), None)
    
    @classmethod
    def get_cache_path(cls, pk):
        return '%s/%s/' % (cls._meta, pk)
    
    @classmethod
    def get(cls, pk):
        if not pk:
            return None
        
        cache_path = cls.get_cache_path(pk)
        record = cache.get(cache_path, None)
        if record is None:
            try:
                record = cls.objects.get(pk=pk, enable=True)
                cache.set(cache_path, record, 3600)
            except cls.DoesNotExist:
                pass
        return record

    @classmethod
    def get_all_cache_path(cls):
        return '%s/ALL/' % (cls._meta)        

    @classmethod
    def get_all(cls):
        cache_path = cls.get_all_cache_path()
        records = cache.get(cache_path, None)
        if records is None:
            try:
                records = cls.objects.filter(enable=True)
                records = list(records)
                cache.set(cache_path, records, 3600)
            except cls.DoesNotExist:
                pass
        return records

class CachedPlayerModel(models.Model):
    '''
    キャッシュに対応したプレイヤーモデル
    抽象モデル
    '''
    
    class Meta:
        abstract = True
        verbose_name = u'キャッシュに対応したプレイヤーモデル'
    
    def __unicode__(self):
        return self.name

    player_id = models.CharField(u'プレイヤーID', max_length=255, default='', primary_key=True)
    enable = models.BooleanField(verbose_name=u'有効', default=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now_add=True, auto_now=True)
    
    def save(self, *args, **kwargs):
        super(CachedPlayerModel, self).save(*args, **kwargs)
        cache.set(self.get_cache_path(self.pk), None)
    
    def delete(self, *args, **kwargs):
        cache.set(self.get_cache_path(self.pk), None)
        super(CachedPlayerModel, self).delete(*args, **kwargs)
    
    @memoized_property
    def player(self):
        from player.models import Player
        return Player.get(self.player_id)
    
    @classmethod
    def get_cache_path(cls, pk):
        return '%s/%s/' % (cls._meta, pk)
    
    @classmethod
    def get(cls, pk):
        if not pk:
            return None
        
        cache_path = cls.get_cache_path(pk)
        record = cache.get(cache_path, None)
        if record is None:
            try:
                record = cls.objects.get(pk=pk, enable=True)
                cache.set(cache_path, record, 3600)
            except cls.DoesNotExist:
                pass
        return record

class CachedMultiPlayerModel(models.Model):
    '''
    キャッシュに対応したマルチプレイヤーモデル
    抽象モデル
    '''
    
    class Meta:
        abstract = True
        verbose_name = u'キャッシュに対応したマルチプレイヤーモデル'
    
    def __unicode__(self):
        return self.name

    player_id = models.CharField(u'プレイヤーID', max_length=255, default='', db_index=True)
    enable = models.BooleanField(verbose_name=u'有効', default=True)
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(u'更新日時', auto_now_add=True, auto_now=True)
    
    def save(self, *args, **kwargs):
        super(CachedMultiPlayerModel, self).save(*args, **kwargs)
        cache.set(self.get_cache_path(self.pk), None)
        cache.set(self.get_cache_filter_by_path(self.player_id), None)
    
    def delete(self, *args, **kwargs):
        cache.set(self.get_cache_path(self.pk), None)
        cache.set(self.get_cache_filter_by_path(self.player_id), None)
        super(CachedMultiPlayerModel, self).delete(*args, **kwargs)
    
    @memoized_property
    def player(self):
        from player.models import Player
        return Player.get(self.player_id)
    
    @classmethod
    def get_cache_path(cls, pk):
        return '%s/%s/' % (cls._meta, pk)
    
    @classmethod
    def get(cls, pk):
        if not pk:
            return None
        
        cache_path = cls.get_cache_path(pk)
        record = cache.get(cache_path, None)
        if record is None:
            try:
                record = cls.objects.get(pk=pk, enable=True)
                cache.set(cache_path, record, 3600)
            except cls.DoesNotExist:
                pass
        return record
    
    @classmethod
    def get_cache_filter_by_path(cls, player_id):
        return '%s/FILTER/%s/' % (cls._meta, player_id)
    
    @classmethod
    def get_filter_by_player(cls, player_id):
        if not player_id:
            return None
        
        cache_path = cls.get_cache_filter_by_path(player_id)
        records = cache.get(cache_path, None)
        if records is None:
            try:
                records = cls.objects.filter(player_id=player_id, enable=True)
                records = list(records)
                cache.set(cache_path, records, 3600)
            except cls.DoesNotExist:
                pass
        return records


def include(include_path):
    """
    :param
        include_path (extension.module.item.models.effect.ItemEffect)
    :return:
        module
    """
    if include_path is None:
        return None

    module_path = '.'.join(include_path.split('.')[:-1])

    try:
        module = __import__(module_path)
    except ImportError:
        return None
    else:
        for path in include_path.split('.')[1:]:
            try:
                module = getattr(module, path)
            except AttributeError:
                return None

        return module

class FakeMasterModelMeta(type):
    """
    extensionにfixturesが定義してあればそれを優先に使う
    """
    def __new__(mcls, name, bases, attrs):
        cls = type.__new__(mcls, name, bases, attrs)
        if name == 'FakeMasterModel':
            return cls

        cls_module = cls.__module__
        if '.'.join(cls_module.split('.')[:1]) == "extension":
            cls_module = '.'.join(cls_module.split('.')[1:])

        excls = include('extension.%s.%s' % (cls_module, cls.__name__))

        if excls:
            cls.fixtures = excls.fixtures

        return cls

class FakeMasterModel(object):
    """
    マスターデータだが DB に保存するほどでもないモデル.

    fixtures プロパティに含まれるディクショナリから,
    オブジェクトのプロパティを生成する.
    """
    __metaclass__ = FakeMasterModelMeta

    fixtures = {}

    class DoesNotExist(Exception):
        pass

    def __init__(self, pk):
        fixture = self.fixtures.get(pk)

        if fixture is None:
            raise self.DoesNotExist(pk)

        for attr in ['pk', 'id']:
            setattr(self, attr, pk)

        for attr in fixture:
            setattr(self, attr, fixture[attr])

    @classmethod
    def get(cls, pk):
        return cls(pk)

    @classmethod
    def get_all(cls):
        return [cls(pk) for pk in cls.fixtures.iterkeys()]
