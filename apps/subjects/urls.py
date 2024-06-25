from django.urls import path

from apps.subjects import views

urlpatterns = [
    path('', views.SubjectListView.as_view(), name='subjects_list-page'),

    path('resource/', views.ResourceListView.as_view(), name='resources_list-page'),
    path('resource/create/', views.ResourceCreateView.as_view(), name='resources_create-page'),
    path('resource/delete/<int:pk>', views.ResourceDeleteView.as_view(), name='resources_delete-page'),
    path('resource/update/<int:pk>', views.ResourceUpdateView.as_view(), name='resources_update-page'),
]
