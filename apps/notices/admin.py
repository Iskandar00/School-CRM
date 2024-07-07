from django.contrib import admin

from apps.notices.models import ChatMessage, Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'recipient_email', 'recipient_phone_number', 'recipient_full_name',
                    'sender_email', 'sender_phone_number', 'sender_full_name',)
    list_display_links = list_display
    fields = ('recipient', 'sender',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'message', 'created_at', 'is_viewed',)
    list_display_links = list_display
    fields = ('chat', 'sender', 'message', 'is_viewed',)
