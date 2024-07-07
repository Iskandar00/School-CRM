from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.subjects.models import Resource, Subject
from apps.subjects.forms import SubjectCreateForm


class SubjectListView(ListView):
    template_name = 'all-subject.html'
    extra_context = {'form': SubjectCreateForm}

    def post(self):
        self.request.POST.get()

    def get_queryset(self):
        queryset = Subject.objects.all()
        search_id = self.request.GET.get('search_id')
        name = self.request.GET.get('name')
        published_at = self.request.GET.get('creating_date')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if published_at:
            queryset = queryset.filter(published_at=published_at)
        return queryset


class ResourceListView(ListView):
    template_name = 'all-book.html'

    def get_queryset(self):
        queryset = Resource.objects.all()
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')
        creating_date = self.request.GET.get('creating_date')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(
                Q(name__icontains=search_name)
            )
        if creating_date:
            queryset = queryset.filter(created_at=creating_date)
        return queryset


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
