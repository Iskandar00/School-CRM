from django.urls import path

from apps.subjects.views import SubjectListView, ResourceListView

urlpatterns = [
    path('', SubjectListView.as_view(), name='subjects_list-page'),
    path('resource/', ResourceListView.as_view(), name='resources_list-page'),
]
