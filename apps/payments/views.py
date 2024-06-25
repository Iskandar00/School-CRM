from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.payments.models import Payment


class PaymentListView(ListView):
    model = Payment
    template_name = 'all-fees.html'


class PaymentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Payment
    fields = ['teacher', 'student', 'year', 'month', 'salary', 'in_percent', ]

    template_name = 'admit-form.html'
    permission_required = ('payments.add_payment',)
    success_url = reverse_lazy('payments_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Payment'
        return context


class PaymentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Payment
    template_name = 'users_delete.html'
    permission_required = ('payments.delete_payment',)
    success_url = reverse_lazy('payments_list-page')


class PaymentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Payment
    fields = ['teacher', 'student', 'year', 'month', 'salary', 'in_percent', ]
    template_name = 'users_update.html'
    permission_required = ('payments.change_payment',)
    success_url = reverse_lazy('payments_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Payment'
        return context
