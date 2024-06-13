from django.urls import path

from apps.general.views import HomeTemplateView, MapTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home-page'),
    path('map/', MapTemplateView.as_view(), name='map-page'),
]
