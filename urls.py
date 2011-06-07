from django.conf.urls.defaults import *
from dtl import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^biblioteka/', include('biblioteka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'dtl.views.list_books'),
  #  (r'^books/(?P<page>\d+)/$', 'dtl.views.book_detail'),
    (r'^detail/(?P<book_id>\d+)/$', 'dtl.views.book_detail'),
    (r'^author/(?P<author_id>\d+)/$', 'dtl.views.author_detail'),
    (r'^category/(?P<category_id>\d+)/$', 'dtl.views.category_detail'),
    (r'^search/$', 'dtl.views.search'),
    (r'^dash/$', 'dtl.views.dashboard'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
