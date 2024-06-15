import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.general.models import AbstractModel
from apps.users.models import CustomUser


class Payment(AbstractModel):

    class MonthChoices(models.IntegerChoices):
        January = 1, 'january'
        February = 2, 'february'
        March = 3, 'march'
        April = 4, 'april'
        May = 5, 'may'
        June = 6, 'june'
        July = 7, 'july'
        August = 8, 'august'
        September = 9, 'september'
        October = 10, 'october'
        November = 11, 'november'
        December = 12, 'december'

    teacher = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.Teacher.value},
                                on_delete=models.PROTECT, blank=True, null=True, related_name='teacher_payments')
    student = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.Student.value},
                                on_delete=models.PROTECT, blank=True, null=True, related_name='student_payments')
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2005), MaxValueValidator(datetime.date.today().year + 1)],
        default=datetime.datetime.now().year)
    month = models.PositiveSmallIntegerField(choices=MonthChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    in_percent = models.PositiveSmallIntegerField(default=100)

    def clean(self):
        if not (1 <= self.in_percent <= 100):
            raise ValidationError({'in_percent': '[1 : 100]-oraliqda kiriting!!!'})

        if (bool(self.teacher) + bool(self.student)) != 1:
            raise ValidationError('Teacher yoki student birini tanlang')

    def __str__(self):
        if self.teacher:
            return f'{self.teacher}: {self.in_percent}'
        return f'{self.student}: {self.in_percent}'

    class Meta:
        unique_together = (('year', 'month', 'teacher'), ('year', 'month', 'student'))











