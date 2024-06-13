from django.urls import path

from apps.users import views

urlpatterns = [
    path('students/', views.StudentsListView.as_view(), name='students_list-page'),
    path('students-create/', views.StudentCreateView.as_view(), name='students_create-page'),
    path('students-create/<int:pk>', views.StudentDeleteView.as_view(), name='students_delete-page'),
    path('student-detail/<int:pk>', views.StudentDetailView.as_view(), name='student_detail-page'),
    path('student-update/<int:pk>', views.StudentUpdateView.as_view(), name='student_update-page'),

    path('teachers/', views.TeachersListView.as_view(), name='teachers_list-page'),
    path('teacher-detail/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_detail-page'),

    path('parents/', views.ParentsListView.as_view(), name='parents_list-page'),
    path('parent-detail/<int:pk>', views.ParentDetailView.as_view(), name='parent_detail-page'),


    path('profile-admin', views.AdminTemplateView.as_view(), name='profile-admin'),
    path('profile-student', views.StudentTemplateView.as_view(), name='profile-student'),
    path('profile-parent', views.ParentTemplateView.as_view(), name='profile-parent'),
    path('profile-teacher', views.TeacherTemplateView.as_view(), name='profile-teacher'),


    path('users-account/', views.UserCreateView.as_view(), name='users-account-page'),


    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
