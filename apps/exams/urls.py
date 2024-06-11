from django.urls import path

from apps.exams.views import ExamListView, ExamResultListView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam_list-page'),
    path('exam_result/', ExamResultListView.as_view(), name='exam_result_list-page')
]
