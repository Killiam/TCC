from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blog.models import Artigo
from blog.feeds import UltimosArtigos

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index',
        {'queryset': Artigo.objects.all(), 'date_field': 'publicacao'}),
    (r'^admin/(.*)', admin.site.root),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': {'ultimos': UltimosArtigos}}),
    (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
    (r'^contato/$', 'views.contato'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^teta/$', 'vagas.views.index'),
    (r'^/teste/1(?P<object_id>\d+)/$', 'vagas.views.detail'),

)


if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

