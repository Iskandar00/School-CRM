from django.db.models import Q
from django.views.generic import ListView

from apps.lessons.models import Lesson


class LessonsListView(ListView):
    template_name = 'lessons/all-lessons.html'

    def get_queryset(self):
        queryset = Lesson.objects.all()
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')
        content = self.request.GET.get('creating_date')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(
                Q(title__icontains=search_name)
            )
        if content:
            queryset = queryset.filter(created_at=content)
        return queryset
