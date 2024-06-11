from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('role', 'first_name', 'last_name', 'gender',
                    'father_name', 'mother_name', 'date_of_birth', 'email',)
    list_display_links = list_display
    list_filter = ('first_name', 'last_name', 'gender', 'father_name', 'mother_name', 'date_of_birth', 'email')
    readonly_fields = []
    fields = [('first_name', 'last_name'), 'role', 'password', 'email', 'phone_number',
              'user_permissions', 'is_staff', 'last_login', 'gender', 'father_name', 'mother_name', 'salary',
              'student_group', 'date_of_birth',
              'child', 'address', ]
