from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from apps.notices.forms import MessageForm
from apps.notices.models import Notification, Chat, ChatMessage


class MessageListView(LoginRequiredMixin, ListView):
    template_name = 'chat.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Chat.objects.filter(Q(recipient_id=user.id) | Q(sender_id=user.id)).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        chat_id = self.request.GET.get('chat_id')
        if chat_id:
            context['chat'] = ChatMessage.objects.filter(chat_id=chat_id).last()
            context['chat_messages'] = ChatMessage.objects.filter(chat_id=chat_id).order_by('is_viewed', 'created_at')
        else:
            context['chat'] = None

        return context

    def post(self, request, *args, **kwargs):
        chat_id = request.GET.get('chat_id')
        message = request.POST.get('message')
        if chat_id and message:
            form = MessageForm({'chat': int(chat_id), 'sender': request.user.pk, 'message': message})
            if form.is_valid():
                form.save()
            else:
                messages.error(request, form.errors)
        else:
            messages.error(request, 'from is not valid.')
        return redirect(request.META['HTTP_REFERER'])

class NotificationCreateView(CreateView):
    template_name = 'chat.html'
    model = Notification
    fields = '__all__'
    success_url = 'users-account-page'
