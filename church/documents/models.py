from django.db import models
from django.db.models import permalink
from django.conf import settings
from tagging.fields import TagField
from django.utils.translation import ugettext_lazy as _

import tagging

class Type(models.Model):
    """Document model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    still = models.FileField(upload_to='document_type_stills', blank=True, help_text='An image that will be used as a thumbnail.')
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'document_types'
        verbose_name_plural = 'types'

    def __unicode__(self):
        return '%s' % self.title


class DocumentSet(models.Model):
    """DocumentSet model"""
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    documents = models.ManyToManyField('Document', related_name='document_sets')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'document_sets'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('document_set_detail', None, { 'slug': self.slug })


class Document(models.Model):
    """Document model"""
    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    types = models.ForeignKey(Type)
    still = models.FileField(upload_to='documents/document_stills', blank=True, help_text='An image that will be used as a thumbnail.')
    document = models.FileField(upload_to='documents/files')
    description = models.TextField(blank=True)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    tags = TagField()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'documents'
        verbose_name_plural = 'documents'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
      return ('document_detail', None, { 'slug': self.slug })