# -*- coding: utf-8 -*-

from django.core.cache import cache
from django.core.urlresolvers import reverse

from opensocial.templatetags.osmobile import opensocial_url_convert

class BackHistoryConstant(object):
    CATEGORY_EQUIPMENT = 1
    CATEGORIES = (
        (CATEGORY_EQUIPMENT, u'装備')
    )

class BackHistoryManager(object):
    """
    履歴管理マネージャー
    """
    
    @classmethod
    def _get_history_key(cls, category_id):
        return 'BackHistoryManager/history/%s' % (category_id)
    
    @classmethod
    def get_history_url(cls, category_id):
        """
        category_id: ConstantのカテゴリID
        """
        key = cls._get_history_key(category_id)
        val = cache.get(key, None)
        
        if not val or not isinstance(val, dict):
            return None, None
        
        if not 'view' in val or not 'args' in val or not 'title' in val:
            return None, None
        
        return opensocial_url_convert(reverse(val['view'], args=val['args'])), val['title']
    
    @classmethod
    def set_history_url(cls, category_id, title, view, args=[]):
        """
        category_id: ConstantのカテゴリID
        view: 戻り先のurls.pyのnameを文字列で
        args: viewに渡す引数をリスト形式で
        """
        key = cls._get_history_key(category_id)
        
        val = {
            'view': view,
            'args': args,
            'title': title,
        }
        
        cache.set(key, val, 1800)
    
    @classmethod
    def del_history_url(cls, category_id):
        """
        category_id: ConstantのカテゴリID
        """
        key = cls._get_history_key(category_id)
        
        cache.delete(key)
    