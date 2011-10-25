from django.contrib import admin
from documents.models import *


class DocumentSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(DocumentSet, DocumentSetAdmin)

class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Document, DocumentAdmin)

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Type, TypeAdmin)
