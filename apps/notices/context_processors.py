from django.db.models import Q

from apps.notices.models import ChatMessage


def get_messages(request):
    user_messages = ChatMessage.objects.filter(Q(chat__recipient_id=request.user.pk)
                                               |
                                               Q(chat__sender_id=request.user.pk)
                                               ).exclude(sender_id=request.user.pk).order_by('-created_at')[0:5]
    print(user_messages)
    return {'user_messages': user_messages}
