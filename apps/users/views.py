from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from apps.users.models import CustomUser


class StudentsListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value)
    template_name = 'all-student.html'


class StudentDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value)
    template_name = 'student-details.html'


class TeachersListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value)
    template_name = 'all-teacher.html'


class TeacherDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value)
    template_name = 'teacher-details.html'


class ParentsListView(ListView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Parent.value)
    template_name = 'all-parents.html'


class ParentDetailView(DetailView):
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.Parent.value)
    template_name = 'parents-details.html'


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
