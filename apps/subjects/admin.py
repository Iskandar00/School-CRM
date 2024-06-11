from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.subjects.models import Subject, Resource


@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ('price', 'name', 'published_at',)
    prepopulated_fields = {'slug': ['name']}

    list_display_links = list_display
    list_filter = ('price', 'name', 'published_at',)
    group_fieldsets = True


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'author', 'name', 'url', 'published_at',)
    list_display_links = list_display
    list_select_related = ('subject',)
    list_filter = ('subject', 'author', 'name',)
