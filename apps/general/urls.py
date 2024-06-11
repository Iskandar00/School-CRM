from django.urls import path

from apps.general.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home-page')
]
