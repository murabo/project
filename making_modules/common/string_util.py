# -*- coding: utf-8 -*-

import re

class StringUtil(object):
    '''
    文字列処理のユーティリティクラス
    '''
    
    @classmethod
    def escape_for_django(cls, text):
        'Djangoの特殊文字をHTMLエスケープ'
        text = re.sub('{', '&#123;', text)
        text = re.sub('}', '&#125;', text)
        text = re.sub('\'', '&#39;', text)
        text = re.sub('"', '&quot;', text)
        text = re.sub('†', '&dagger;', text)
        text = re.sub('\r', '', text)
        text = re.sub('\n', '', text)
        return text
        