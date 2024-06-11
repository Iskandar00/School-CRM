from django.urls import path

from apps.attendances.views import AttendanceListView

urlpatterns = [
    path('', AttendanceListView.as_view(), name='attendances_list-page')
]
