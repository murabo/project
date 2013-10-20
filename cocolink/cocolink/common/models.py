# -*- coding: utf-8 -*-
from django.db import models

from django.core.cache import cache
from cocolink.common.memoized_property import memoized_property

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
