from django.contrib import admin

from apps.exams.models import Exam, ExamResult


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'month', 'limit_hour',)
    list_display_links = list_display
    list_select_related = ('subject',)
    list_filter = ('subject', 'month',)


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'percent', 'comment',)
    list_display_links = list_display
    list_select_related = ('student', 'exam',)
    list_filter = ('student', 'exam',)
