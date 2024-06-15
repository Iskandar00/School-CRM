from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from apps.users.models import CustomUser


# ================= Students_View_Detail Start==================

class StudentsListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value)
    template_name = 'all-student.html'


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'gender', 'image', 'date_of_birth', 'email',
              'phone_number', 'password', 'student_group', 'address', ]

    template_name = 'admit-form.html'
    permission_required = ('users.add_customuser',)
    success_url = reverse_lazy('students_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Students'
        return context

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.Student
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users_delete.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('students_list-page')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'gender', 'image', 'date_of_birth', 'email',
              'phone_number', 'password', 'student_group', 'address', ]
    template_name = 'users_update.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('students_list-page')


class StudentDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value)
    template_name = 'student-details.html'


# ================= Students_View_Detail End==================


# ================= Teachers_View_Detail Start==================

class TeachersListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value)
    template_name = 'all-teacher.html'


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'salary', 'email',
              'phone_number', 'password', 'address', ]

    template_name = 'admit-form.html'
    permission_required = ('users.add_customuser',)
    success_url = reverse_lazy('teachers_list-page')

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


# ================= Parents_View_Detail Start==================

class ParentsListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Parent.value)
    template_name = 'all-parents.html'


#
class ParentsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'child', 'email',
              'phone_number', 'password', 'address', ]

    template_name = 'admit-form.html'
    permission_required = ('users.add_customuser',)
    success_url = reverse_lazy('parents_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Parents'
        return context

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.Parent
        return super().form_valid(form)


class ParentsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'users_delete.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('parents_list-page')


class ParentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'child', 'email',
              'phone_number', 'password', 'address', ]
    template_name = 'users_update.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('parents_list-page')


class ParentDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Parent.value)
    template_name = 'parents-details.html'


# ================= Parents_View_Detail End==================


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home-page')
        return super().get(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class AdminTemplateView(TemplateView):
    template_name = 'index.html'


class TeacherTemplateView(TemplateView):
    template_name = 'index5.html'


class StudentTemplateView(TemplateView):
    template_name = 'index3.html'


class ParentTemplateView(TemplateView):
    template_name = 'index4.html'


class UserCreateView(CreateView):
    template_name = 'account-settings.html'
    model = CustomUser
    fields = '__all__'
    success_url = 'users-account-page'
