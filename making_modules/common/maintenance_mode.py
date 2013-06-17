# -*- coding: utf-8 -*-

"""
メンテナンスモードミドルウェア

sangokuでの実装を参考に作成。
-テストプレイヤー以外のユーザの場合、メンテ中画面を表示する
 (テストプレイヤーはDjango管理画面で OSUSER 単位で設定)
-状態の値はTTに保存
-運用向け管理画面でメンテ状態を変更できる
-メンテナンスモード中、定義されたユーザの時はメンテ中ヘッダが挿入される

1) admin モデルを用意
管理画面でいじれるようにするモデル

2) メンテ中画面用テンプレートを用意
error/maintenance.html
※process_request() で指定

3) admin用テンプレート追加
admin/admin/settings_index.html

4) urls.py に以下追加
    # 管理画面用URL
    (r'^admin/admin/', include('gokudo.admin.admin_urls')),

5) テストプレイヤーを用意
Django管理画面の「テストプレイヤー」に,関係者のものを追加する
※sangokuの場合、settings.py でOSUSER_IDのリストが定義され、これでユーザ判定している

6) settings.MIDDLEWARE_CLASSES に
'common.maintenance_mode.MaintenanceModeMiddleware'
を追加

"""

import sys
import re
import logging

from gokudo.admin.manager import MaintainanceStatusManager,is_specify_users
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from notification.models import get_notice

from opensocial.http import HttpResponseOpensocialRedirect
from django.core.urlresolvers import reverse




def check_maintenance(request):
    '''
    maintenanceモードの判定
    '''
    
    MaintenanceModeMiddleware.display_header = False
    maintenance_status = MaintainanceStatusManager.get_session()
    if request.path.startswith('/m/notice/'):
        return None
    if request.path.startswith('/m/maintenance/'):
        return None
    if not request.path.startswith('/m/'):
        return None
    if maintenance_status == 0:
        import logging
        logging.debug(request)
        if not is_specify_users(request):
            # コールバック系はエラーを返す
            if request.path.startswith('/m/gacha/purchase_callback/') or request.path.startswith('/m/shop/purchase_callback/'):
                return HttpResponse(status = 403)

            return HttpResponseOpensocialRedirect(reverse('mobile_maintenance'))
#                # 運営からのお知らせ
#                notice_list = get_notice(limit=3)
#                ctxt = RequestContext(request,{
#                    "message": u'只今メンテナンスモードです。少々お待ち下さい。',
#                    "notice_list": notice_list,
#                })
#                return render_to_response('error/maintenance.html', ctxt) 
        else:
            MaintenanceModeMiddleware.display_header = True

    return None

def maintenance_judge(view_func):
    def decorate(request, *args, **kwds):
        
        redirect_response = check_maintenance(request)
        if redirect_response:
            return redirect_response
        
        return view_func(request, *args, **kwds)
        decorate.__doc__ = view_func.__doc__
        decorate.__dict__ = view_func.__dict__
    return decorate


class MaintenanceModeMiddleware:
    """
    "Maintenance Mode" middleware 4 check GAME o/ Specific users: 
    0 -> メンテナンスモード 1 -> 公開中
    """

    def __init__(self):
        self.display_header = False

#    def process_request(self, request):
#        self.display_header = False
#        maintenance_status = MaintainanceStatusManager.get_session()
#        if request.path.startswith('/m/notice/'):
#            return None
#        if request.path.startswith('/m/maintenance/'):
#            return None
#        if not request.path.startswith('/m/'):
#            return None
#        if maintenance_status == 0:
#            import logging
#            logging.debug(request)
#            if not is_specify_users(request):
#                # コールバック系はエラーを返す
#                if request.path.startswith('/m/gacha/purchase_callback/') or request.path.startswith('/m/shop/purchase_callback/'):
#                    return HttpResponse(status = 403)
#                
#                return HttpResponseOpensocialRedirect(reverse('mobile_maintenance'))
##                # 運営からのお知らせ
##                notice_list = get_notice(limit=3)
##                ctxt = RequestContext(request,{
##                    "message": u'只今メンテナンスモードです。少々お待ち下さい。',
##                    "notice_list": notice_list,
##                })
##                return render_to_response('error/maintenance.html', ctxt) 
#            else:
#                self.display_header = True
#
#        return None

    def process_response(self, request, response):
        """
        メンテナンスモードで許可ユーザの場合、ヘッダ追加
        """
        if request.path.startswith('/admin/'):
            return response

        if hasattr(MaintenanceModeMiddleware, 'display_header') and MaintenanceModeMiddleware.display_header:
            content = response.content
            content = self.insertMeintenanceHeader(content)
            response.content = content
        return response

    def insertMeintenanceHeader(self, document):
        message = '<div align="center">Maintenance Mode Now!</div>'
        pattern = re.compile("(<body.*?>)(.*?)(</body.*?>)", re.DOTALL)
        ret = re.sub(pattern, r"\1" + message + r"\2\3", document)
        return ret

