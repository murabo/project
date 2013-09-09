# coding:utf-8
from cocolink.myuser.models import MyUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def login_execute(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse("login_success"),)
        else:
            # Return a 'disabled account' error message
            return HttpResponseRedirect(reverse("login_error"),)
    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect(reverse("login_error"),)

@login_required
def login_success(request):
    """
    ログイン完了画面表示用
    """
    
    ctxt = RequestContext(request, 
                          {"username":request.user.username,
                                    })
    return render_to_response("html/login_success.html",ctxt)

def login_error(request):
    """
    ログイン完了画面表示用
    """
    return render_to_response("html/login_error.html",)

def sign_up_execute(request):
    """
    会員登録処理
    """
    """
    if 既にDBにあったなら:
        エラー
    """ 
    ctxt = RequestContext(request, {})
    print "AAAAA", ctxt
    MyUser.objects.all()
    user = User.objects.create_user()
    