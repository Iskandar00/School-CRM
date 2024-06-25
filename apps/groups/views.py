from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from apps.groups.models import StudentGroup


class GroupListView(ListView):
    model = StudentGroup
    template_name = 'all-class.html'


class StudentGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]

    template_name = 'admit-form.html'
    permission_required = ('student_group.add_student_group',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class StudentGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StudentGroup
    template_name = 'users_delete.html'
    permission_required = ('student_group.delete_student_group',)
    success_url = reverse_lazy('group_list-page')


class StudentGroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]
    template_name = 'users_update.html'
    permission_required = ('student_group.change_payment',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class GroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'all-group-student.html'
