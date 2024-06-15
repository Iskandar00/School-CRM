from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from apps.general.models import AbstractModel
from apps.general.services import normalize_text
from apps.general.validate import phone_number_validate
from apps.users.managers import CustomUserManager


class CustomUser(AbstractUser, AbstractModel):
    class RoleChoices(models.TextChoices):
        Admin = 'admin'
        Teacher = 'teacher'
        Student = 'student'
        Parent = 'parent'

    class GenderChoices(models.TextChoices):
        Male = 'male'
        Female = 'female'

    objects = CustomUserManager()

    username = None

    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    image = models.ImageField(upload_to='users/image', blank=True, null=True)
    # oylik
    salary = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)], default=0,
                                 blank=True, null=True)
    father_name = models.CharField(max_length=75)
    mother_name = models.CharField(max_length=75, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # role = student
    student_group = models.ForeignKey('groups.StudentGroup', on_delete=models.PROTECT, blank=True, null=True,
                                      related_name='students')

    # role = parent
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    phone_number = models.CharField(max_length=13, validators=[phone_number_validate], unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=2000)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['role', 'first_name', 'last_name', 'email', ]

    def __str__(self):
        return f'{self.get_role_display()}-{self.first_name}-{self.last_name}'

    def clean(self):
        super().clean()
        if self.role == self.RoleChoices.Teacher.value and self.salary is None:
            raise ValidationError({'salary': 'Salary kiriting'})

        if self.role == self.RoleChoices.Student.value and self.student_group is None:
            raise ValidationError({'student_group': 'Student_group kiriting'})

        if self.role == self.RoleChoices.Parent.value and self.child is None:
            raise ValidationError({'child': 'Child kiriting'})



