from django.contrib import admin

from apps.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'year', 'month', 'created_at', 'salary', 'in_percent',)
    list_display_links = list_display
    list_select_related = ('teacher', 'student',)
    list_filter = ('teacher', 'student', 'year', 'created_at', 'salary', 'in_percent',)
