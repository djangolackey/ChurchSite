from django.db import models
from django.db.models import permalink
from django.conf import settings
from tagging.fields import TagField
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField, USPhoneNumberField
from basic.profiles.models import Profile
from django.contrib.auth.models import Group
from django.contrib.localflavor.us.models import PhoneNumberField, USStateField

import tagging

class Family(models.Model):
    """Family model"""
    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    photo = models.FileField(upload_to='family_photos', blank=True, help_text='An image that will be used as a thumbnail.')
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    address = models.CharField(max_length=256, blank=True)
    address2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = USStateField(blank=True, default='AR')
    zip = models.CharField(_('zip'), blank=True, max_length=10)
    phone1 = PhoneNumberField(_('phone'), blank=True)
    phone2 = PhoneNumberField(_('other phone'), blank=True)
    email = models.CharField(max_length=256, blank=True)
    website = models.URLField(max_length=256, blank=True)
    notes = models.TextField(blank=True)
    tags = TagField()

    class Meta:
        db_table = 'membership_families'
        verbose_name_plural = 'families'

    def __unicode__(self):
        return '%s family' % self.name

    @permalink
    def get_absolute_url(self):
      return ('family_detail', None, { 'slug': self.slug })

class Member(models.Model):
    """Member model"""
    STATUS_CHOICES = (
        (0, 'Removed'),
        (1, 'Member'),
        (2, 'Friend'),
    )
    METHOD_CHOICES = (
        (0, 'None'),
        (1, 'Baptism'),
        (2, 'Letter'),
    )
    profile = models.OneToOneField(Profile, primary_key=True)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    family = models.ForeignKey(Family, blank=True, null=True)
    lives_with_family = models.BooleanField(help_text='Check if family address is sufficient contact.')
    photo = models.FileField(upload_to='member_photos', blank=True, help_text='An image that will be used as a thumbnail.')
    date_joined = models.DateField(blank=True, null=True)
    method = models.IntegerField(_('method'), choices=METHOD_CHOICES, default=1, help_text="If a member, how was membership confirmed")
    date_baptised = models.DateField(blank=True, null=True)
    conversion_story = models.TextField(blank=True)
    notes = models.TextField(blank=True, help_text="Notes should not be made public")
    tags = TagField()

    class Meta:
        db_table = 'membership_members'
        verbose_name = 'members and friends'
        verbose_name_plural = 'members and friends'
        permissions = (
              ("view_data", "Can view member data"),
        )

    def __unicode__(self):
        if self.status == 1:
            return '%s membership information' % self.profile.user.get_full_name()
        else:
            return '%s information' % self.profile.user.get_full_name()

    @permalink
    def get_absolute_url(self):
        return ('profile_detail', None, { 'username': self.profile.user.username })

    def save(self, *args, **kwargs):
        super(Member, self).save(*args, **kwargs)
        if self.status == 1:
            group=Group.objects.get(name='member')
            self.profile.user.groups.add(group)
        if self.status == 2:
            group=Group.objects.get(name='friend')
            self.profile.user.groups.add(group)

class Office(models.Model):
    """Office model"""
    STATUS_CHOICES = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    member = models.ManyToManyField(Member, blank=True, null=True)
    official_photo = models.FileField(upload_to='officer_photos', blank=True, help_text='An image that will be used as a thumbnail.')
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    last_filled_date = models.DateField(blank=True, null=True)
    contact_email = models.CharField(max_length=256, blank=True)
    office_responsibilities = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    tags = TagField()

    class Meta:
        db_table = 'membership_offices'
        verbose_name_plural = 'offices'

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
      return ('office_detail', None, { 'slug': self.slug })
