# coding:utf-8
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def sign_up_view(request):
    """
    会員登録画面表示処理
    """
    # TODO tryしておかないと、セッションが無い場合こける。違う方法もありそう。
    try:
        login = request.session["login"]
    except:
        login = None

    # loginしていた場合、どこに飛ばす？
    if login:
        # TODO log
        return HttpResponseRedirect(reverse("index_view"),)

#    request.session["login"] = True
#    print request.session["login"]
    # TODO log
    return render_to_response("html/sign_up.html",)

def sign_up_execute(request):
    """
    会員登録処理
    """
    """
    if 既にDBにあったなら:
        エラー
    """ 
    user = User.objects.create_user()
    