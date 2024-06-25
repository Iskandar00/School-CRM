from django.urls import path

from apps.lessons.views import LessonsListView

urlpatterns = [
    path('', LessonsListView.as_view(), name='lessons_list-page'),
]
