from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cocolink.views.index_view', name='index_view'),
    url(r'^sign_in/$', 'cocolink.views.sign_in_view', name='sign_in_view'),
    url(r'^post/$', 'cocolink.views.post_view', name='post_view'),
    url(r'^test/$', 'cocolink.views.test_view', name='test_view'),
    url(r'^sign_up/$', 'cocolink.myuser.views.sign_up_view', name='sign_up_view'),
    url(r'^sign_up_execute/$', 'cocolink.myuser.views.sign_up_execute', name='sign_up_execute'),
    # url(r'^cocolink/', include('cocolink.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                            )
urlpatterns += staticfiles_urlpatterns()