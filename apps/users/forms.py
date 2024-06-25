from django import forms

from apps.users.models import CustomUser


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'gender', 'image', 'date_of_birth', 'email',
                  'phone_number', 'password', 'longitude', 'latitude', 'student_group', 'address', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TeacherRegisterForm(StudentRegisterForm):
    class Meta(StudentRegisterForm.Meta):
        fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'salary', 'email',
                  'phone_number', 'password', 'longitude', 'latitude', 'address', ]


class ParentRegisterForm(StudentRegisterForm):
    class Meta(StudentRegisterForm.Meta):
        fields = ['first_name', 'last_name', 'father_name', 'gender', 'image', 'date_of_birth', 'child', 'email',
                  'phone_number', 'password', 'longitude', 'latitude', 'address', ]
