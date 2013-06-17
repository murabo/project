# -*- coding: utf-8 -*-

import time
import logging
import traceback
import sys
from functools import wraps

from django.db import connection
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import mail_admins

from gamelog.decorators import _get_event_type, _log_event_access

from opensocial.models import OpenSocialUser, get_osuser
from opensocial.decorators import get_for_update

from common.sorry_page import (
    _get_hostname,
    _get_osuser_name,
    _get_sandbox_sign,
    _get_system_name,
    ERROR_MAIL_SUBJECT_TEMPLATE,
    ERROR_MAIL_MESSAGE_TEMPLATE,
    _mail_admins_exception
)

from player.models import Player


class FunctionDebugger(object):
    
    @staticmethod
    def debug_sql(func):
        '''
        発行したSQLをdebugに書き出すデコレータ
        デバッグ用
        '''
        def decorate(*args, **kw):
            start_time = time.time()
            connection.queries = []
            ret = func(*args, **kw)
            delta = time.time() - start_time
            for query in connection.queries:
                logging.debug('SQL[%(sql)s], TIME[%(time)s]' % query)
            return ret
        return decorate
    
    @staticmethod
    def debug_time(func):
        '''
        メソッド実行時の時間をデバッグ
        '''
        def decorate(*args, **kw):
            start_time = time.time()
            ret = func(*args, **kw)
            delta = time.time() - start_time
            logging.debug('[%s] end. %sms' % (func.func_name,int(delta*1000)))
            return ret
        return decorate
    
    
    @staticmethod
    def debug_args(func):
        '''
        メソッド実行時の引数をデバッグ出力
        時間も計測する
        '''
        def decorate(*args, **kw):
            start_time = time.time()
            logging.debug('[%s] start. args=%r, kw=%r' % (func.func_name, args, kw))
            ret = func(*args, **kw)
            delta = time.time() - start_time
            logging.debug('[%s] end. %sms' % (func.func_name,int(delta*1000)))
            return ret
        return decorate
    

def no_simultaneous_access(view_func):
    def decorate(request, *args, **kwds):
        assert hasattr(request, 'opensocial_userid'), "require_osuser requires singned_request or oauth_signature_required decolator."
        # OpenSocialUserを取得する
        try:
            osuser = get_for_update(OpenSocialUser.objects, pk=request.opensocial_userid)
        except:
            _mail_admins_no_simul(request)
            request.player = Player.get(request.opensocial_userid)
            ctxt = RequestContext(request,{
                    'player': request.player,
                    })
        
            return render_to_response('root/no_simultaneous_access.html', ctxt)
        view_functions = view_func(request, *args, **kwds)
        osuser.save()
        return view_functions
    return decorate


def log_event_dau(event_type_id):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            player = request.player
            try:
                event_type = _get_event_type(event_type_id)
                _log_event_access(player.osuser_id, event_type)
            except Exception, e:
                if not hasattr(settings, 'OPENSOCIAL_DEBUG'):
                    _mail_admins_exception(request, e)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def _mail_admins_no_simul(request):
    """
    例外をADMINSにメール
    django/core/handlers/base.py  147 def handle_uncaught_exception を真似した
    @return: None
    """
    try: 
        request_repr = repr(request) 
    except: 
        request_repr = "Request repr() unavailable"
    
    values = {
        'SANDBOX_SIGN' : _get_sandbox_sign(),
        'SYSTEM_NAME' : _get_system_name(),
        'HOSTNAME' : _get_hostname(),
        'EXCEPTION_TYPE' : u'NoSimultaneousAccess',
        'EXCEPTION_MESSAGE': u'no_simultaneous_access exception.',
        'OSUSER' : _get_osuser_name(request),
        'REQUEST_PATH' : request.path,
        'TRACEBACK_LOG' : '\n'.join(traceback.format_exception(*sys.exc_info())),
        'REQUEST_REPR' : request_repr,
    }
    try:
        subject = ERROR_MAIL_SUBJECT_TEMPLATE % values
    except UnicodeDecodeError:
        subject = u'subject unavalable(UnicodeDecodeError) %r' % values
    try:
        message = ERROR_MAIL_MESSAGE_TEMPLATE % values
    except UnicodeDecodeError:
        message = u'message unavalable(UnicodeDecodeError)\n%r' % values
    #mail_admins(subject, message, fail_silently=True)
    mail_admins(subject, message)

