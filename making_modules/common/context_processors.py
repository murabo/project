# -*- coding: utf-8 -*-
import urllib
from django.conf import settings
from opensocial.templatetags.osmobile import opensocial_url_convert
from common.static_values import StaticValues
from point.constants import PointStatic

from eventmodules.components.comp_gameevent.constants import GameEventConstant

opensocial_gps_url = '/m/area/gps/'
if not settings.OPENSOCIAL_DEBUG:
    if settings.OPENSOCIAL_CONTAINER == 'mixi.jp':
        opensocial_gps_url = 'location:cell' + opensocial_url_convert(urllib.quote(opensocial_gps_url))
    elif settings.OPENSOCIAL_CONTAINER[-7:] == 'mbga.jp':
        opensocial_gps_url = 'location:self' + opensocial_url_convert(urllib.quote(opensocial_gps_url)) + '&amp;type=cell'
    elif settings.OPENSOCIAL_CONTAINER[-7:] == 'gree.jp':
        opensocial_gps_url = 'location:cell' + opensocial_url_convert(urllib.quote(opensocial_gps_url))

opensocial_invite_url = '/m/invite/'
if not settings.OPENSOCIAL_DEBUG:
    if settings.OPENSOCIAL_CONTAINER == 'mixi.jp':
        opensocial_invite_url = 'invite:friends?callback=' + urllib.quote(
            'http://' + settings.SITE_DOMAIN + opensocial_invite_url)
    elif settings.OPENSOCIAL_CONTAINER[-7:] == 'mbga.jp':
        opensocial_invite_url = 'invite:friends?guid=ON&url=' + urllib.quote(
            'http://' + settings.SITE_DOMAIN + opensocial_invite_url)
    elif settings.OPENSOCIAL_CONTAINER[-7:] == 'gree.jp':
        opensocial_invite_url = 'invite:friends?callback=' + urllib.quote(
            'http://' + settings.SITE_DOMAIN + opensocial_invite_url)

def contexts(request):
    return { 'opensocial_app_id'  : request.REQUEST.get('opensocial_app_id'),
             'opensocial_owner_id': request.REQUEST.get('opensocial_owner_id'),
             'app_id' : settings.APP_ID,
             'app_name' : settings.APP_NAME,
             'opensocial_domain'  : 'ma.mixi.net',
             'opensocial_gps_url' : opensocial_gps_url,
             'opensocial_invite_url' : opensocial_invite_url,
             'domain'             : settings.SITE_DOMAIN,
             'escaped_path' : request.path.replace('/', '%2F'),
             'debug': settings.DEBUG,
             'enable_kvs': settings.ENABLE_KVS,
             'open_friends': settings.OPEN_FRIENDS,
             'opensocial_sandbox' : settings.OPENSOCIAL_SANDBOX,
             'opensocial_allow_from_pc' : settings.OPENSOCIAL_ALLOW_FROM_PC,
             'SV' : StaticValues,
             'MSV' : GameEventConstant,
             'admin_site_name' : settings.ADMIN_SITE_NAME,
             'admin_css' : settings.ADMIN_CSS_LINK,
             'point_static': PointStatic('point'),
             'money_static': PointStatic('money'),
             'medal_static': PointStatic('medal'),
             }
