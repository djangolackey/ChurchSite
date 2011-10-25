from django.contrib.syndication.feeds import FeedDoesNotExist
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.models import Comment
from django.core.urlresolvers import reverse
from basic.blog.models import Post, Category

from django.shortcuts import get_object_or_404


class BlogPostsFeed(Feed):
    _site = Site.objects.get_current()
    title = '%s feed' % _site.name
    description = '%s posts feed.' % _site.name

    def link(self):
        return reverse('blog_index')

    def items(self):
        return Post.objects.published()[:10]

    def item_pubdate(self, obj):
        return obj.publish

    def item_description(self, obj):
        return obj.tease


class BlogPostsByCategory(Feed):
    _site = Site.objects.get_current()
    title = '%s posts category feed' % _site.name

    def get_object(self, request, slug):
        return get_object_or_404(Category, slug__exact=slug)

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return obj.get_absolute_url()

    def description(self, obj):
        return "Posts recently categorized as %s" % obj.title

    def items(self, obj):
        return obj.post_set.published()[:10]

    def item_pubdate(self, obj):
        return obj.publish

    def item_description(self, obj):
        return obj.tease