from django.urls import path

from apps.users import views

urlpatterns = [
    path('students/', views.StudentsListView.as_view(), name='students_list-page'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student_detail-page'),
    path('teachers/', views.TeachersListView.as_view(), name='teachers_list-page'),
    path('teacher-detail/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_detail-page'),
    path('parents/', views.ParentsListView.as_view(), name='parents_list-page'),
    path('parent-detail/<int:pk>', views.ParentDetailView.as_view(), name='parent_detail-page'),

    path('profile-admin', views.AdminTemplateView.as_view(), name='profile-admin'),
    path('profile-student', views.StudentTemplateView.as_view(), name='profile-student'),
    path('profile-parent', views.ParentTemplateView.as_view(), name='profile-parent'),
    path('profile-teacher', views.TeacherTemplateView.as_view(), name='profile-teacher'),


    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
