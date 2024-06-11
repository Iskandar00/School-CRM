from django.contrib import admin

from apps.attendances.models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'status', 'attendance_date')
    list_display_links = list_display
    list_select_related = ('student',)
    list_filter = ('student',)
