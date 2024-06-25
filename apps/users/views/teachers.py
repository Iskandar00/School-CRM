from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView

from apps.users.forms import TeacherRegisterForm
from apps.users.models import CustomUser


# ================= Teachers_View_Detail Start==================
class TeacherTemplateView(TemplateView):
    template_name = 'index5.html'


class TeachersListView(ListView):
    template_name = 'all-teacher.html'

    def get_queryset(self):
        queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value)
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')
        search_phone_number = self.request.GET.get('search_phone_number')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(
                Q(first_name__icontains=search_name)
                |
                Q(last_name__icontains=search_name)
                |
                Q(father_name__icontains=search_name)
            )
        if search_phone_number:
            queryset = queryset.filter(phone_number__endswith=search_phone_number)
        return queryset


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()

    template_name = 'admit-form.html'
    permission_required = ('users.add_customuser',)
    success_url = reverse_lazy('teachers_list-page')
    form_class = TeacherRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Teachers'
        return context

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.Teacher
        return super().form_valid(form)


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users_delete.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('teachers_list-page')


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'salary', 'email',
              'phone_number', 'password', 'address', ]
    template_name = 'users_update.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('teachers_list-page')


class TeacherDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value)
    template_name = 'teacher-details.html'

# ================= Teachers_View_Detail End==================
