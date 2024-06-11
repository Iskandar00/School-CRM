from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.general.urls')),
    path('groups/', include('apps.groups.urls')),
    path('subjects/', include('apps.subjects.urls')),
    path('attendances/', include('apps.attendances.urls')),
    path('exams/', include('apps.exams.urls')),
    path('users/', include('apps.users.urls')),
    path('payments/', include('apps.payments.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    path('', include('apps.general.urls')),
    path('groups/', include('apps.groups.urls')),
    path('subjects/', include('apps.subjects.urls')),
    path('attendances/', include('apps.attendances.urls')),
    path('exams/', include('apps.exams.urls')),
    path('users/', include('apps.users.urls')),
    path('payments/', include('apps.payments.urls')),
)
