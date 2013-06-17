#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

ANDROID_VER = re.compile('Android (\d+\.?\d+)')

CONVERT_STR = re.compile(u'([に弟備])([\s<\n&])')

class AndroidIcsMiddleware(object):
    
    def process_response(self, request, response):
        
        if not request.path.startswith("/m/"):
            return response
        
        content_type = response.get('Content-Type',"")
        if not content_type.startswith("text/html"):
            return response
        
        content = response.content
        
        if not content:
            return response
        
        user_agent = request.META.get('HTTP_USER_AGENT', "")
        
        ver = 0
        match_str = ANDROID_VER.search(user_agent)
        if match_str and len(match_str.groups()) > 0:
            ver = float(match_str.group(1))
            
        if ver >= 4.0:
            content = self.apply(content)
        
        response.content = content
        return response

    def apply(self, document):

        if isinstance(document,str):
            document = unicode(document,'utf-8','ignore')
        
        result = self.changeText(document)

        return result

    # 特定文字列単体を置換
    def changeText(self, document):
        document = CONVERT_STR.sub(ur'\1&nbsp;\2', document)

        return document
