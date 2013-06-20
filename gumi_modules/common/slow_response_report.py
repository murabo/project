# -*- coding: utf-8 -*-

"""
システムの応答時間を計測するミドルウェア
"""

import logging
import time

from django.db import connection
from django.conf import settings
from django.core.mail import mail_admins
from gokudo.gu3.error_mail import get_hostname

REPORT_THRESHOLD = 5.00

MAIL_SUBJECT_TEMPLATE = u"""%(SANDBOX_SIGN)s%(SYSTEM_NAME)s Slow response (%(ELAPSED_TIME).2fs) in %(REQUEST_PATH)s"""

MAIL_MESSAGE_TEMPLATE = u"""\
system_name:
    %(SANDBOX_SIGN)s%(SYSTEM_NAME)s

hostname:
    %(HOSTNAME)s

elapsed_time:
    %(ELAPSED_TIME).2fs

osuser:
    %(OSUSER)s

request_path:
    %(REQUEST_PATH)s

user_agent:
    %(HTTP_USER_AGENT)s
"""

slow_response_logger = logging.getLogger('slow_response')
#sql_logger = logging.getLogger('sql')

class SlowResponseReportMiddleware(object):
    """
    スローレスポンスをレポート
    """
    def process_request(self, request):
        request.response_report_start_time = time.time()
    
    def process_response(self, request, response):
        
        if not request.path.startswith("/m/"):
            return response
        
        content_type = response.get('Content-Type',"")
        if ((not content_type.startswith('text/html') and
             not content_type.startswith('application/xhtml+xml')) or
            getattr(response, 'status_code') != 200):
            return response
        
        if hasattr(request, 'response_report_start_time'):
            elapsed_time = time.time() - request.response_report_start_time
            if elapsed_time > REPORT_THRESHOLD:
                logging.warn('[SlowResponseReportMiddleware] elapsed_time: %.3f %s' % (elapsed_time, request.path))
                if settings.MAIL_ON_SLOW_RESPONSE_TIMES:
                    mail_message = '[SLOW_RESPONSE] elapsed_time:%.3f, host:%s, osuser:%s' % (elapsed_time, get_hostname(), str(request.opensocial_userid))
                    mail_admins(mail_message, mail_message + (u". REQUEST_PATH: %s" % request.path))
                #slow_response_logger.info('[SLOW_RESPONSE] elapsed_time:%.3f, host:%s, osuser:%s, path:%s, ' % (elapsed_time, getattr(settings,'HOSTNAME',''), _get_osuser_name(request), request.path))
                
            if settings.DEBUG:
                
                total_sql_time = sum([ float(q['time']) for q in connection.queries])
                total_sql_count = len(connection.queries)
                
                if all((
                    hasattr(request, 'outside_of_decorators_start_time'),
                    hasattr(request, 'outside_of_decorators_end_time'),
                    hasattr(request, 'inside_of_decorators_start_time'),
                    hasattr(request, 'inside_of_decorators_end_time'),
                    )):
                    # raiseされた場合はend_timeがつかない。
                    # デコレータで時間を記録している場合、詳細な時間経過をレポート
                    time_string = 'M2D: %.3f, D2V:%.3f, V:%.3f, V2D:%.3f, D2M:%.3f, T:%.3f' % (
                        request.outside_of_decorators_start_time - request.response_report_start_time,
                        request.inside_of_decorators_start_time - request.outside_of_decorators_start_time,
                        request.inside_of_decorators_end_time - request.inside_of_decorators_start_time,
                        request.outside_of_decorators_end_time - request.inside_of_decorators_end_time,
                        time.time() - request.outside_of_decorators_end_time,
                        time.time() - request.response_report_start_time,
                    )
                    html_elapsed_time_report = '<div style="text-align:right;" align="right">%s, %dSQLs(%.2fs)</div>' %\
                     (time_string, total_sql_count, total_sql_time)
                else:
                    # デコレータを仕込んでない場合
                    html_elapsed_time_report = '<div style="text-align:right;" align="right">Gen:%.2fs, %dSQLs(%.2fs)</div>' %\
                     (elapsed_time, total_sql_count, total_sql_time)
                response.content = response.content.replace('</body>', '%s</body>' % html_elapsed_time_report)
                
                #if getattr(settings, 'SQL_DEBUG', False):
                #    for query in connection.queries:
                #        sql_logger.debug('%s %s %s' % (request.path, query['time'], query['sql']))
        
        return response
    
    
    @staticmethod
    def outside_of_decorators(func):
        """
        デコレータの最外部に入れておくと、ミドルウェアの入出力の速度を計測する
        """
        def decorate(request, *args, **kw):
            request.outside_of_decorators_start_time = time.time()
            ret = func(request, *args, **kw)
            request.outside_of_decorators_end_time = time.time()
            return ret
        return decorate
    
    @staticmethod
    def inside_of_decorators(func):
        """
        デコレータの最内部に入れておくと、デコレータの速度とビュー関数の速度を計測する
        """
        def decorate(request, *args, **kw):
            request.inside_of_decorators_start_time = time.time()
            ret = func(request, *args, **kw)
            request.inside_of_decorators_end_time = time.time()
            return ret
        return decorate




def _get_osuser_name(request):
    """
    osuser名
    """
    try:
        osuser = request.osuser
        return "%s:%s" % (osuser.userid, osuser.nickname)
    except:
        return "Osuser unavailable."
