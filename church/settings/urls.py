from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.simple.direct_to_template', { 'template': 'base.html' }),
#    (r'^accounts/', include('registration.urls')),
#    (r'^grappelli/', include('grappelli.urls')),
)

#Tagging models
from basic.blog.models import Post
from basic.bookmarks.models import Bookmark
from basic.events.models import Event
from basic.media.models import Video, Audio
from photologue.models import Photo
from basic.places.models import Place
from documents.models import Document

urlpatterns += patterns('tagging.views',
   url(r'^links/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Bookmark.objects.all(), 'extra_context': {'type': 'bookmarks',},'template_name': 'tagging/bookmarks_by_tag.html'}),
   url(r'^events/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Event.objects.all(), 'extra_context': {'type': 'events',},'template_name': 'tagging/events_by_tag.html'}),
   url(r'^tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Photo.objects.filter(is_public=True),'template_name': 'photos_by_tag.html'}),
   url(r'^videos/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Video.objects.all(), 'extra_context': {'type': 'videos',},'template_name': 'tagging/videos_by_tag.html'}),
   url(r'^audioclips/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Audio.objects.all(), 'extra_context': {'type': 'audioclips',},'template_name': 'tagging/audios_by_tag.html'}),
   url(r'^places/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Place.objects.filter(status=1), 'extra_context': {'type': 'places',},'template_name': 'tagging/places_by_tag.html'}),
   url(r'^documents/tags/(?P<tag>[-\w]+)/$', 'tagged_object_list', {'queryset_or_model': Document.objects.filter(status=1), 'extra_context': {'type': 'documents',},'template_name': 'tagging/documents_by_tag.html'}),
)

urlpatterns += patterns('',
     (r'^accounts/', include('registration.backends.default.urls')),
     (r'^links/', include('basic.bookmarks.urls')),
     (r'^books/', include('basic.books.urls')),
     (r'^comments/', include('basic.comments.urls')),
     (r'^events/', include('basic.events.urls')),
     (r'^flag/', include('basic.flagging.urls')),
     (r'^groups/', include('basic.groups.urls')),
     (r'^invitations/', include('basic.invitations.urls')),
     (r'^photos/', include('photologue.urls')),
     (r'^videos/', include('basic.media.urls.videos')),
     (r'^audioclips/', include('basic.media.urls.audios')),
     (r'^messages/', include('basic.messages.urls')),
     (r'^movies/', include('basic.movies.urls')),
     (r'^music/', include('basic.music.urls')),
     (r'^people/', include('basic.people.urls')),
     (r'^places/', include('basic.places.urls')),
     (r'^people/', include('basic.people.urls')),
     (r'^relationships/', include('basic.relationships.urls')),
     (r'^pastors-pen/', include('basic.blog.urls')),
     (r'^profiles/', include('basic.profiles.urls')),
     (r'^documents/', include('documents.urls')),
     (r'^notify/', include('notification.urls')),
     (r'^families/', include('churchmembers.urls')),
)

urlpatterns += patterns('',
    (r'',           include('django.contrib.flatpages.urls')),
)
