from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.groups.models import StudentGroup


class GroupListView(ListView):
    model = StudentGroup
    template_name = 'all-class.html'


class GroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'all-group-student.html'
