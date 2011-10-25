from django.conf.urls.defaults import *
from basic.media.models import *


audio_list = {
    'queryset': Audio.objects.all(),
}
audio_set_list = {
    'queryset': AudioSet.objects.all(),
}


urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^sets/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=audio_set_list,
        name='audio_set_detail',
    ),
    url(r'^sets/$',
        view='object_list',
        kwargs=audio_set_list,
        name='audio_set_list',
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=audio_list,
        name='audio_detail',
    ),
    url (r'^$',
        view='object_list',
        kwargs=audio_list,
        name='audio_list',
    ),
)