from django.urls import path

from apps.payments.views import PaymentListView, PaymentCreateView, PaymentDeleteView, PaymentUpdateView

urlpatterns = [
    path('', PaymentListView.as_view(), name='payments_list-page'),
    path('create/', PaymentCreateView.as_view(), name='payments_create-page'),
    path('delete/<int:pk>/', PaymentDeleteView.as_view(), name='payments_delete-page'),
    path('update/<int:pk>/', PaymentUpdateView.as_view(), name='payments_update-page'),
]
