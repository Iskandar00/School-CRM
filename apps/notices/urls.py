from django.urls import path

from apps.notices.views import MessageCreateView, NotificationCreateView

urlpatterns = [
    path('', NotificationCreateView.as_view(), name='notifications_list-page'),
    path('messages/', MessageCreateView.as_view(), name='messages_list-page'),
]
