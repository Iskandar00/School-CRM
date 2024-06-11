from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.users.models import CustomUser


class Attendance(models.Model):
    class StatusChoices(models.TextChoices):
        Because_of = 'because_of'
        Without_reason = 'without_reason'
        Came = 'came'

    student = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE,
                                limit_choices_to={'role': CustomUser.RoleChoices.Student.value}, )
    status = models.CharField(max_length=30, choices=StatusChoices.choices)
    attendance_date = models.DateField()
    reason = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return f'{self.student} {self.status}'

    class Meta:
        unique_together = ('student', 'attendance_date')
