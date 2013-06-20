# -*- coding: utf-8 -*-
import datetime
import time
from django.conf import settings

class TerminalLogger(object):

    @classmethod
    def level_color(cls, status):
        return {
            "DEBUG": "\033[22;32m",
            "INFO": "\033[01;34m",
            "WARNING": "\033[22;35m", 
            "ERROR": "\033[22;31m",
            "CRITICAL": "\033[01;31m",
            "NORMAL": "\033[0;0m"
        }.get(status)

    @classmethod
    def printlog(cls, string, level="DEBUG"):
        if not settings.DEBUG:
            return

        if not settings.OPENSOCIAL_ALLOW_FROM_PC:
            return

        logs = []
        if not isinstance(string, list):
            logs.append(string)
        else:
            logs = logs + string
        for log in logs:
            decoded_string = None
            print "[" + cls.level_color(level) + log + cls.level_color("NORMAL") + "]"
 
    @classmethod
    def debug_log(cls, string):
        cls.printlog(string, "DEBUG")
 
    @classmethod
    def info_log(cls, string):
        cls.printlog(string, "INFO")
 
    @classmethod
    def warning_log(cls, string):
        cls.printlog(string, "WARNING")
 
    @classmethod
    def critical_log(cls, string):
        cls.printlog(string, "CRITICAL")
 
    @classmethod
    def normal_log(cls, string):
        cls.printlog(string, "NORMAL")
             
