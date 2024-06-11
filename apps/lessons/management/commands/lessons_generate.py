from django.core.management import BaseCommand

from apps.lessons.models import Lesson
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1, 4):
            Lesson.objects.create(subject=Subject.objects.filter(name='Backend').last(),
                                  title=f'Paython_{i}',
                                  ordering_number=f'{i}',
                                  content=f'Dasturlash asoslari_{i}', )

            Lesson.objects.create(subject=Subject.objects.filter(name='Frontend').last(),
                                  title=f'HTML_{i}',
                                  ordering_number=f'{i}',
                                  content=f'HTML asoslari_{i}', )

            Lesson.objects.create(subject=Subject.objects.filter(name='AI').last(),
                                  title=f'Sifatli content_{i}',
                                  ordering_number=f'{i}',
                                  content=f'Boshlang\'ich tushunchalar_{i}', )

        self.stdout.write(self.style.SUCCESS('lessons created'))
