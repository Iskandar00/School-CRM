from django.contrib import admin

from apps.groups.models import StudentGroup


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', 'created_at',)
    list_display_links = list_display
    list_select_related = ('subject', 'teacher',)
    list_filter = ('subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', 'created_at',)
