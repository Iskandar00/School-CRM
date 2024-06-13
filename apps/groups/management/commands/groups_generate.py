from django.core.management import BaseCommand

from apps.groups.models import StudentGroup
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        teacher = CustomUser.objects.filter(role=CustomUser.RoleChoices.Teacher.value).last()

        StudentGroup.objects.create(subject=Subject.objects.filter(name='Backend').last(),
                                    teacher=teacher,
                                    start_time='10:00',
                                    end_time='12:00',
                                    week_days=[0, 2, 4],
                                    create_date='2024-06-10', )

        StudentGroup.objects.create(subject=Subject.objects.filter(name='Frontend').last(),
                                    teacher=teacher,
                                    start_time='12:00',
                                    end_time='14:00',
                                    week_days=[1, 3, 5],
                                    create_date='2024-06-10', )

        StudentGroup.objects.create(subject=Subject.objects.filter(name='AI').last(),
                                    teacher=teacher,
                                    start_time='14:00',
                                    end_time='15:00',
                                    week_days=[0, 1, 2, 3, 4],
                                    create_date='2024-06-10', )

        self.stdout.write(self.style.SUCCESS('student_group created'))

        student = CustomUser.objects.create_user(role='student',
                                                 password='2',
                                                 first_name='Simba',
                                                 last_name='Mufassayev',
                                                 gender='male',
                                                 father_name='Mufassayevich',
                                                 student_group=StudentGroup.objects.filter(
                                                     subject__name='Backend').last(),
                                                 phone_number='+998901254567',
                                                 email='b1@b.bb',
                                                 address='Chilonzor')
        student.groups.set([1])
        parent = CustomUser.objects.create_user(role='parent',
                                                password='4',
                                                first_name=f'Mufassa',
                                                last_name=f'Sherov',
                                                gender=f'male',
                                                father_name='Sherbek',
                                                child_id=student.pk,
                                                phone_number='+998991235567',
                                                email='d1@d.dd',
                                                address=f'Sergely')
        parent.groups.set([4])
        self.stdout.write(self.style.SUCCESS('student and parent created'))
