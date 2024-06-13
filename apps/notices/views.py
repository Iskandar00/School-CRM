from django.shortcuts import render
from django.views.generic import CreateView

from apps.notices.models import Notification, Message


class NotificationCreateView(CreateView):
    template_name = 'notice-board.html'
    model = Notification
    fields = '__all__'
    success_url = 'users-account-page'


class MessageCreateView(CreateView):
    template_name = 'messaging.html'
    model = Message
    fields = '__all__'
    success_url = 'users-account-page'
