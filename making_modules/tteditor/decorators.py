# -*- coding: utf-8 -*-

from functools import wraps

from django.http import HttpResponseForbidden

def superuser_required(view_func):
    """
    スーパーユーザーのみ許可
    """
    @wraps(view_func)
    def decorate(request, *args, **kwds):
        if not request.user.is_superuser:
            return HttpResponseForbidden(u'アクセスが許可されていません')
        return view_func(request, *args, **kwds)
    return decorate