from django.conf.urls.defaults import *
from churchmembers.models import Family


family_list = {
    'queryset': Family.objects.filter(status=1),
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=family_list,
        name='family_detail',
    ),
    url (r'^$',
        view='object_list',
        kwargs=family_list,
        name='family_list',
    ),
)

urlpatterns += patterns('churchmembers.views',
    url(r'^update/$',
        view='family_info_form',
        name='family_form',
    ),
)