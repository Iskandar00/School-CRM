from django.core.exceptions import ValidationError
from django.db import models

from apps.general.models import AbstractModel
from apps.general.services import normalize_text
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class Exam(AbstractModel):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    month = models.PositiveSmallIntegerField()
    limit_hour = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.subject}: {self.month}-month'

    class Meta:
        unique_together = ('subject', 'month')


class ExamResult(AbstractModel):
    student = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.Student.value},
                                on_delete=models.SET_NULL, null=True)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    percent = models.PositiveSmallIntegerField()
    comment = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return f'{self.student}: {self.exam}'

    @classmethod
    def get_normalize_fields(cls):
        return ['comment']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def clean(self):
        if not (1 <= self.percent <= 100):
            raise ValidationError({'percent': '[1 : 100]-oraliqda kiriting!!!'})

    class Meta:
        unique_together = ('student', 'exam')
