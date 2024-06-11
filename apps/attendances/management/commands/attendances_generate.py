from django.core.management import BaseCommand

from apps.attendances.models import Attendance
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        student = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value).last()
        Attendance.objects.create(student=student,
                                  status=Attendance.StatusChoices.Because_of.value,
                                  attendance_date=f'2024-06-10', )

        Attendance.objects.create(student=student,
                                  status=Attendance.StatusChoices.Without_reason.value,
                                  attendance_date=f'2024-06-11',
                                  reason=f'Hammasi nazorat ostida!!!')

        Attendance.objects.create(student=student,
                                  status=Attendance.StatusChoices.Came.value,
                                  attendance_date=f'2024-06-12', )

        self.stdout.write(self.style.SUCCESS('attendances created'))
