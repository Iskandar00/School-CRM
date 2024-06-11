from django.shortcuts import render
from django.views.generic import ListView

from apps.payments.models import Payment


class PaymentListView(ListView):
    model = Payment
    template_name = 'all-fees.html'
