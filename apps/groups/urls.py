from django.urls import path

from apps.groups.views import GroupListView, GroupDetailView

urlpatterns = [
    path('', GroupListView.as_view(), name='group_list-page'),
    path('group_detail/<int:pk>', GroupDetailView.as_view(), name='group_detail-page')
]
