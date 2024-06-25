from django.urls import path

from .views import admins, students, parents, teachers, auth

urlpatterns = [
    path('students/', students.StudentsListView.as_view(), name='students_list-page'),
    path('students-create/', students.StudentCreateView.as_view(), name='students_create-page'),
    path('students-delete/<int:pk>', students.StudentDeleteView.as_view(), name='students_delete-page'),
    path('student-detail/<int:pk>', students.StudentDetailView.as_view(), name='student_detail-page'),
    path('student-update/<int:pk>', students.StudentUpdateView.as_view(), name='student_update-page'),

    path('teachers/', teachers.TeachersListView.as_view(), name='teachers_list-page'),
    path('teacher-create/', teachers.TeacherCreateView.as_view(), name='teachers_create-page'),
    path('teacher-delete/<int:pk>/', teachers.TeacherDeleteView.as_view(), name='teachers_delete-page'),
    path('teacher-detail/<int:pk>/', teachers.TeacherDetailView.as_view(), name='teacher_detail-page'),
    path('teacher-update/<int:pk>/', teachers.TeacherUpdateView.as_view(), name='teachers_update-page'),

    path('parents/', parents.ParentsListView.as_view(), name='parents_list-page'),
    path('parents-create/', parents.ParentsCreateView.as_view(), name='parents_create-page'),
    path('parent-delete/<int:pk>', parents.ParentsDeleteView.as_view(), name='parent_delete-page'),
    path('parent-update/<int:pk>', parents.ParentUpdateView.as_view(), name='parent_update-page'),
    path('parent-detail/<int:pk>', parents.ParentDetailView.as_view(), name='parent_detail-page'),

    path('profile-admin', admins.AdminTemplateView.as_view(), name='profile-admin'),
    path('profile-student', students.StudentTemplateView.as_view(), name='profile-student'),
    path('profile-parent', parents.ParentTemplateView.as_view(), name='profile-parent'),
    path('profile-teacher', teachers.TeacherTemplateView.as_view(), name='profile-teacher'),

    path('users-account/', admins.UserCreateView.as_view(), name='users-account-page'),

    path('login/', auth.CustomLoginView.as_view(), name='login'),
    path('logout/', auth.CustomLogoutView.as_view(), name='logout'),
]
