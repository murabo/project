# coding:utf-8

from django.shortcuts import render_to_response

def index_view(request):
    return render_to_response("html/input_user.html",)