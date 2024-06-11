from django.urls import path

from apps.payments.views import PaymentListView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payments_list-page'),
]
