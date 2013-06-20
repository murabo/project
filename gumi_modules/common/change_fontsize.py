#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class ChangeFontSizeMiddleware(object):
    def __init__(self):
        self.agent = "ezweb"
        self.is_vga = False

    def process_response(self, request, response):
        
        if not request.path.startswith("/m/"):
            return response
        
        content_type = response.get('Content-Type',"")
        if not content_type.startswith("text/html"):
            return response
        
        content = response.content
        
        if not content:
            return response
        
        device = request.device
        
        if device.is_docomo():
            self.setAgentDocomo()
        elif device.is_ezweb():
            self.setAgentEzweb()
        elif device.is_softbank():
            if request.device.display.is_vga():
                self.setAgentSoftBankVga()
            else:
                self.setAgentSoftBank()
        else:
            self.agent = 'smartphone'
            
        content = self.apply(content)
        
        response.content = content
        return response


    def setAgentDocomo(self):
        self.agent = "docomo"

    def setAgentEzweb(self):
        self.agent = "ezweb"

    def setAgentSoftBank(self):
        self.agent = "softbank"

    def setAgentSoftBankVga(self):
        self.agent = "softbank"
        self.is_vga = True

    def apply(self, document, base_dir = None, agent = None, is_vga = False):
        if agent:
            self.agent = agent

        if is_vga:
            self.is_vga = is_vga

        if isinstance(document,str):
            document = unicode(document,'utf-8','ignore')
        
        result = self.changeFontSize(document)

        return result

    # キャリア対応 font-size 書き換え
    def changeFontSize(self, document):
        # docomo,auの場合
        if self.agent == "docomo":
            document = self.reFontSize(document, "large", "medium")

        elif self.agent == "ezweb":
            document = self.reFontSize(document, "large", "medium")
            document = self.reFontSize(document, "xx-small", "x-small")

        # softbankの場合
        elif self.agent == "softbank":
            if self.is_vga:
                document = self.reFontSize(document, "medium", "large")
                document = self.reFontSize(document, "xx-small", "medium")
            elif not self.is_vga:
                document = self.reFontSize(document, "large", "medium")
                document = self.reFontSize(document, "xx-small", "x-small")
        
        # Android
        else:
            document = self.reFontSize(document, "xx-small", "medium")

        return document

    # font-size を置換
    def reFontSize(self, document, pattern, repl):
        pattern = "font-size:" + pattern
        repl = "font-size:" + repl
        return re.sub(pattern, repl, document)
