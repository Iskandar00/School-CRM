from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.subjects.models import Resource, Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'all-subject.html'


class ResourceListView(ListView):
    model = Resource
    template_name = 'all-book.html'


class ResourceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Resource
    fields = ['subject', 'author', 'name', 'url', 'published_at', 'month', ]

    template_name = 'admit-form.html'
    permission_required = ('subjects.add_resource',)
    success_url = reverse_lazy('resources_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Resource'
        return context


class ResourceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Resource
    template_name = 'users_delete.html'
    permission_required = ('subjects.delete_resource',)
    success_url = reverse_lazy('resources_list-page')


class ResourceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Resource
    fields = ['subject', 'author', 'name', 'url', 'published_at', 'month', ]
    template_name = 'users_update.html'
    permission_required = ('subjects.change_resource',)
    success_url = reverse_lazy('resources_list-page')
