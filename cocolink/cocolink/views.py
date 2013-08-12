# coding:utf-8

from django.shortcuts import render_to_response

def index_view(request):
    del request.session["login"] 
    return render_to_response("dummy.html",)

def sign_in_view(request):
    return render_to_response("html/sign_in.html",)

def post_view(request):
    return render_to_response("html/post.html",)

def test_view(request):
    return render_to_response("html/test.html",)