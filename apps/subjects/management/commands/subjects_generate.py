from django.core.management import BaseCommand

from apps.subjects.models import Subject, Resource


class Command(BaseCommand):
    def handle(self, *args, **options):
        Subject.objects.create(price=1_500_000,
                               name='Backend',
                               slug='backend',
                               published_at='2005-12-12', )

        Subject.objects.create(price=1_500_000,
                               name='Frontend',
                               slug='frontend',
                               published_at='2005-12-12', )

        Subject.objects.create(price=1_500_000,
                               name='AI',
                               slug='ai',
                               published_at='2005-12-12', )

        self.stdout.write(self.style.SUCCESS('subjects created'))

        Resource.objects.create(subject=Subject.objects.filter(name='Backend').last(),
                                author='Anvar Narzullayev',
                                name='Python, dasturlash asoslari',
                                url='https://python.sariq.dev/', )

        Resource.objects.create(subject=Subject.objects.filter(name='Frontend').last(),
                                author='Iskandar Diyorov',
                                name='"Google" ga hujum',
                                url='https://python.sariq.dev/', )

        Resource.objects.create(subject=Subject.objects.filter(name='AI').last(),
                                author='Fantamas',
                                name='Kitib nomi nimadir',
                                url='https://python.sariq.dev/', )

        self.stdout.write(self.style.SUCCESS('resources created'))
