from django.views.generic import TemplateView, CreateView
from apps.users.models import CustomUser


class AdminTemplateView(TemplateView):
    template_name = 'index.html'


class UserCreateView(CreateView):
    template_name = 'account-settings.html'
    model = CustomUser
    fields = '__all__'
    success_url = 'users-account-page'
