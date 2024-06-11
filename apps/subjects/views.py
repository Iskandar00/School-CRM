from django.shortcuts import render
from django.views.generic import ListView

from apps.subjects.models import Resource, Subject


class SubjectListView(ListView):
    model = Subject
    template_name = 'all-subject.html'


class ResourceListView(ListView):
    model = Resource
    template_name = 'all-book.html'
