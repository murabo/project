from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cocolink.views.index_view', name='index_view'),
    url(r'^sign_in/$', 'cocolink.views.sign_in_view', name='sign_in_view'),
    url(r'^input_user/', 'cocolink.myuser.views.input_user_view', name='input_user_view'),
    # url(r'^cocolink/', include('cocolink.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
