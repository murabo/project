# coding:utf-8

from django.shortcuts import render_to_response
from gu.ajax import ajax_api
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def gu_index(request):

    ctxt = RequestContext(request, 
                          {"username":request.user.username,
                                    })
    return render_to_response("html/gu/index.html",)


def gu_post(request):
    ctxt = ajax_api.insert_post(request)

    result = simplejson.dumps(ctxt, ensure_ascii=False)
    return HttpResponse(result, mimetype='text/javascript')