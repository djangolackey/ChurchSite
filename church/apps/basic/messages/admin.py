from django.contrib import admin
from basic.messages.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'subject', 'to_status', 'from_status', 'created', 'content_type', 'object_id')
admin.site.register(Message, MessageAdmin)
