from django.urls import path

from apps.notices.views import MessageListView, NotificationCreateView

urlpatterns = [
    path('', NotificationCreateView.as_view(), name='notifications_list-page'),
    path('messages/', MessageListView.as_view(), name='messages_list-page'),
]
