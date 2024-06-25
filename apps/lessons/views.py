from django.views.generic import ListView

from apps.lessons.models import Lesson


class LessonsListView(ListView):
    model = Lesson
    template_name = 'lessons/all-lessons.html'