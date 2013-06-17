# -*- coding: utf-8 -*-

from django import forms, template
from django.core.urlresolvers import reverse

register = template.Library()
import logging

@register.inclusion_tag('tteditor/partial/paginator.html', takes_context=True)
def paginator(context, page, url_name, url_param_1=None, url_param_2=None):
    """
    ページネーター
    """
    reverse_args = []
    if url_param_1 is not None:
        reverse_args.append(url_param_1)
    if url_param_2 is not None:
        reverse_args.append(url_param_2)
    
    request = context['request']
    query_string = request.META.get('QUERY_STRING', '')
    if query_string:
        query_string = '?%s' % query_string
    return {
        'url_first_page' : reverse(url_name, args=reverse_args+[1,]) if page.number > 1 else None,
        'url_previous_page' : reverse(url_name, args=reverse_args+[page.previous_page_number(),]) if page.has_previous() else None,
        'url_next_page' : reverse(url_name, args=reverse_args+[page.next_page_number(),]) if page.has_next() else None,
        'page': page,
        'query_string' : query_string,
    }