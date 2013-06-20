# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str

from tteditor.tteditor import TtEditor, TtEditorServer, TtEditorKeyValue, EDIT_MODES
from tteditor.decorators import superuser_required


@login_required
@superuser_required
def index(request):
    """
    TT Editor インデックス
    """
    tte = TtEditor()
    ctxt = RequestContext(request,{
        'tte': tte,
    })
    return render_to_response('tteditor/index.html', ctxt)

@login_required
@superuser_required
def keys_on_server(request, ttname, page_number, per_page=300):
    """
    サーバ内にあるキー一覧
    @param ttname settings.TYRANT_DATABASES のキー名
    """
    page_number = int(page_number)
    ttes = TtEditorServer(ttname)
    
    q = smart_str(request.GET.get('q', ''))
    if q:
        keys = ttes.search_keys(search_word=q)
    else:
        keys = ttes.all_keys
    paginator = Paginator(keys, per_page)
    page = paginator.page(page_number)
    ctxt = RequestContext(request,{
        'ttname' : ttname,
        'ttes' : ttes,
        'paginator' : paginator,
        'page': page,
        'modes' : EDIT_MODES,
        'q' : q,
    })
    return render_to_response('tteditor/keys_on_server.html', ctxt)


@login_required
@superuser_required
def edit(request, ttname, keyname, mode, save_done=False):
    """
    キーの内容編集ページ
    """
    ttekv = TtEditorKeyValue(ttname, keyname, mode)
    ttekv.repr_value
    ctxt = RequestContext(request,{
        'ttekv' : ttekv,
        'ttname' : ttname,
        'keyname' : keyname,
        'mode' : mode,
        'modes' : EDIT_MODES,
        'save_done' : save_done,
    })
    return render_to_response('tteditor/edit.html', ctxt)


@login_required
@superuser_required
def save(request):
    """
    キーの内容保存
    """
    if not request.method == 'POST':
        return HttpResponseBadRequest()
    ttname = request.POST['ttname']
    keyname = request.POST['keyname']
    mode = request.POST['mode']
    value = request.POST['v']
    evaled_value = eval(value) #危険だけど
    ttekv = TtEditorKeyValue(ttname, keyname, mode)
    ttekv.save(evaled_value)
    return_url = reverse('tteditor/save_done', args=[ttname, keyname, mode,])
    return HttpResponseRedirect(return_url)


@login_required
@superuser_required
def delete(request):
    """
    値の削除
    """
    if not request.method == 'POST':
        return HttpResponseBadRequest()
    ttname = request.POST['ttname']
    keyname = request.POST['keyname']
    mode = request.POST['mode']
    ttekv = TtEditorKeyValue(ttname, keyname, mode)
    ttekv.delete()
    return_url = reverse('tteditor/keys_on_server', args=[ttname, 1,])
    return HttpResponseRedirect(return_url)
