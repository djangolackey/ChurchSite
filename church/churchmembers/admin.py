from django.contrib import admin
from churchmembers.models import *
from basic.profiles.admin import ProfileAdmin
from basic.profiles.models import Profile



class FamilyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Family, FamilyAdmin)

class OfficeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Office, OfficeAdmin)

class MemberInline(admin.StackedInline):
    model = Member
    max_num = 1

class NewProfileAdmin(ProfileAdmin):
   inlines = [MemberInline,]

admin.site.unregister(Profile)

admin.site.register(Profile, NewProfileAdmin)