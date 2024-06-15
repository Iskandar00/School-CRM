from django.contrib import admin

from apps.users.models import CustomUser
from django.contrib.auth.models import Permission


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('role', 'first_name', 'last_name', 'gender',
                    'father_name', 'mother_name', 'date_of_birth', 'email',)
    list_display_links = list_display
    list_filter = ('first_name', 'last_name', 'gender', 'father_name', 'mother_name', 'date_of_birth', 'email')
    readonly_fields = []
    fields = [('first_name', 'last_name'), 'role', 'password', 'email', 'phone_number',
              'user_permissions', 'is_staff', 'image', 'gender', 'father_name', 'mother_name', 'salary',
              'student_group', 'date_of_birth',
              'child', 'address', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk or CustomUser.objects.get(pk=obj.pk).password != obj.password:
            obj.set_password(obj.password)
        obj.save()


@admin.register(Permission)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content_type']
