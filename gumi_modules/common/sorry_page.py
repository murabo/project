# -*- coding: utf-8 -*-

"""
ソーリーページミドルウェア

ビューメソッドが出した例外をキャッチし、環境によってトレースバックページを出したりごめんなさいページを出したりする。

■ インストール方法

1)
トレースバック報告用のビューテンプレートと、ソーリーページ用のビューテンプレートを作成して配置。
デフォルトでは、
    error/exception_traceback.html
    error/sorry.html
settings.SORRYPAGE_TEMPLATE_EXCEPTION
settings.SORRYPAGE_TEMPLATE_SORRY
でそれぞれ上書き可能。

2)
settings.MIDDLEWARE_CLASSES に、
     'common.middleware.sorry_page.SorryPageMiddleware', 
を追加。
これ以上は例外が伝わらなくなるので、
devtool.middleware.TracebackMiddleware
なんかはこの下にしておくこと。



"""




import traceback
import sys

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import mail_admins

# TRACEBACK_PAGE_FORCE
# Trueの場合は、どの環境かに関わらずトレースバックページを表示する
# 動作検証用
TRACEBACK_PAGE_FORCE = False


# テンプレートファイルの場所。
# TEMPLATE_EXCEPTION は変数を当てはめるので注意。
TEMPLATE_EXCEPTION = 'root/exception_traceback.html'
if hasattr(settings, 'SORRYPAGE_TEMPLATE_EXCEPTION'):
    TEMPLATE_EXCEPTION = settings.SORRYPAGE_TEMPLATE_EXCEPTION
# TEMPLATE_SORRYはほぼ静的なページ
TEMPLATE_SORRY = 'root/sorry.html'
if hasattr(settings, 'SORRYPAGE_TEMPLATE_SORRY'):
    TEMPLATE_EXCEPTION = settings.SORRYPAGE_TEMPLATE_SORRY

ERROR_MAIL_SUBJECT_TEMPLATE = u"""%(SANDBOX_SIGN)s%(SYSTEM_NAME)s Error. %(EXCEPTION_TYPE)s in %(REQUEST_PATH)s"""

ERROR_MAIL_MESSAGE_TEMPLATE = u"""\
system_name:
    %(SANDBOX_SIGN)s%(SYSTEM_NAME)s

hostname:
    %(HOSTNAME)s

exception_type:
    %(EXCEPTION_TYPE)s

exception_message:
    %(EXCEPTION_MESSAGE)s

osuser:
    %(OSUSER)s

request_path:
    %(REQUEST_PATH)s

----------------------------------------
%(TRACEBACK_LOG)s
----------------------------------------
%(REQUEST_REPR)s
"""




class SorryPageMiddleware(object):
    """
    本番であればごめんなさいページ
    ステージングであればトレースバック
    """
    
    def process_exception(self, request, exception):
        """
        viewで発生した例外をキャッチし、それに応じてページを出力する。
        - ローカル環境
            何もしない。いつものトレースバック出力をする。
            HTTP500になるはず
        - ステージング環境
            トレースバックをHTMLにして返す。
            HTTP200
        - 本番環境
            ごめんなさいページを表示する。
            HTTP200
        ただし、TRACEBACK_PAGE_FORCE が True の場合は、トレースバックページを表示する。
        """
        if TRACEBACK_PAGE_FORCE:
            return _render_traceback_page(request, exception)
        
        if not request.path.startswith("/m/"):
            return None
        
        if settings.DEBUG: #ステージングかローカル
            if settings.OPENSOCIAL_SANDBOX: #ステージング
                _mail_admins_exception(request, exception)
                return _render_traceback_page(request, exception)
            else: #ローカル
                #詳細なトレースバックを表示する
                return None
        else: #本番
            _mail_admins_exception(request, exception)
            if request.path.startswith('/m/gacha/purchase_callback/') or request.path.startswith('/m/shop/purchase_callback/'):
                return None
            return _render_sorry_page(request, exception)




def _render_traceback_page(request, exception):
    """
    トレースバックをHTMLページにして表示
    """
    traceback_log =  '\n'.join(traceback.format_exception(*sys.exc_info()))
    traceback_log_short = '\n'.join(traceback.format_exception(*sys.exc_info())[-3:-1])
    ctxt = RequestContext(request, {
        #'exception_type' : str(type(exception)),
        'exception_type' : exception.__class__.__name__,
        'exception_message' : exception,
        'request_path' : request.path,
        'traceback_log' : traceback_log,
        'traceback_log_short' : traceback_log_short,
    })
    return render_to_response(TEMPLATE_EXCEPTION, ctxt)


def _render_sorry_page(request, exception):
    """
    「ページが表示できません。ごめんなさい。」
    のページを表示。
    """
    ctxt = RequestContext(request, { })
    return render_to_response(TEMPLATE_SORRY, ctxt)





def _mail_admins_exception(request, exception):
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
        'EXCEPTION_TYPE' : exception.__class__.__name__,
        'EXCEPTION_MESSAGE': exception.message,
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


def _get_sandbox_sign():
    if settings.OPENSOCIAL_SANDBOX:
        return u'[SANDBOX] '
    else:
        return u''

def _get_hostname():
    """
    hostname コマンドを発行して、ホスト名を取得
    """
    import subprocess
    try: 
        hostname = subprocess.Popen(["hostname"],stdout=subprocess.PIPE).communicate()[0] 
        hostname = hostname.strip()
    except: 
        hostname = u"Hostname unavailable." 
    return hostname 


def _get_system_name():
    """
    システム名を取得
    """
    try:
        system_name = settings.DATABASES['default']['NAME']
    except:
        system_name = u"SystemName unavailable."
    return system_name


def _get_osuser_name(request):
    """
    osuser名
    """
    try:
        # nickname %sだとエラーが怖いので%rで。
        return u"%s:%r" % (request.osuser.userid, request.osuser.nickname)
    except:
        return u"Osuser unavailable."




