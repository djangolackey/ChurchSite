from django.conf.urls.defaults import *
from documents.models import *


document_list = {
    'queryset': Document.objects.filter(status=1),
}
document_set_list = {
    'queryset': DocumentSet.objects.all(),
}
type_list = {
    'queryset': Type.objects.all(),
}


urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^sets/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=document_set_list,
        name='document_set_detail',
    ),
    url(r'^sets/$',
        view='object_list',
        kwargs=document_set_list,
        name='document_set_list',
    ),
    url(r'^types/(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=type_list,
        name='document_type_detail',
    ),
    url(r'^types/$',
        view='object_list',
        kwargs=type_list,
        name='document_type_list',
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view='object_detail',
        kwargs=document_list,
        name='document_detail',
    ),
    url (r'^$',
        view='object_list',
        kwargs=document_list,
        name='document_list',
    ),
)