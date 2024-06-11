from django.shortcuts import render
from django.views.generic import ListView

from apps.exams.models import Exam, ExamResult


class ExamListView(ListView):
    model = Exam
    template_name = 'exam-schedule.html'


class ExamResultListView(ListView):
    model = ExamResult
    template_name = 'exam-grade.html'
