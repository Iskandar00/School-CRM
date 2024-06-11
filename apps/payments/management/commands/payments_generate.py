from django.core.management import BaseCommand

from apps.payments.models import Payment
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        teacher = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value).last()
        student = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value).last()
        teacher_salary = teacher.salary
        student_salary = student.student_group.subject.price
        for i in range(1, 4):
            Payment.objects.create(teacher=teacher,
                                   month=f'{i}',
                                   salary=teacher_salary, )

            Payment.objects.create(student=student,
                                   month=f'{i}',
                                   salary=student_salary, )

        self.stdout.write(self.style.SUCCESS('payments created'))
