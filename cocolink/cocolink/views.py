# encoding:utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

def index_view(request):
#    del request.session["login"] 
    return render_to_response("dummy.html",)

def sign_in_view(request):
    return render_to_response("html/sign_in.html",)

@csrf_protect
def post_view(request):
    ctxt = RequestContext(request, {})
    return render_to_response("html/post.html",ctxt)

def test_view(request):
    return render_to_response("html/test.html",)