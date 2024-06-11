from django.core.management import BaseCommand

from apps.exams.models import Exam, ExamResult
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        backend = Subject.objects.filter(name='Backend').last()
        frontend = Subject.objects.filter(name='Frontend').last()
        subject = Subject.objects.filter(name='Backend').last()
        for i in range(1, 4):
            Exam.objects.create(subject=subject,
                                month=f'{i}',
                                limit_hour=2, )

            Exam.objects.create(subject=Subject.objects.filter(name='Frontend').last(),
                                month=f'{i}',
                                limit_hour=2, )

            Exam.objects.create(subject=Subject.objects.filter(name='AI').last(),
                                month=f'{i}',
                                limit_hour=2, )

        self.stdout.write(self.style.SUCCESS('exams created'))

        student = CustomUser.objects.filter(role=CustomUser.RoleChoices.Student.value).last()
        exam = Exam.objects.filter(subject_id=student.student_group.subject_id)

        ExamResult.objects.create(student=student,
                                  exam=exam[0],
                                  percent=85, )

        ExamResult.objects.create(student=student,
                                  exam=exam[1],
                                  percent=90, )

        ExamResult.objects.create(student=student,
                                  exam=exam[2],
                                  percent=100, )

        self.stdout.write(self.style.SUCCESS('exam_results created'))
