# coding:utf-8

from django.shortcuts import render_to_response
from cocolink.post.api import ajax_api
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def post(request):
    ctxt = ajax_api.insert_post(request)

    result = simplejson.dumps(ctxt, ensure_ascii=False)
    return HttpResponse(result, mimetype='text/javascript')