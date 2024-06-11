from django.shortcuts import render
from django.views.generic import ListView

from apps.attendances.models import Attendance


class AttendanceListView(ListView):
    model = Attendance
    template_name = 'student-attendence.html'
