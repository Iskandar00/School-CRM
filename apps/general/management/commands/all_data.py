import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        os.system("find . -path '*/migrations/0*' -delete")
        print('makemigrations')
        os.system('python manage.py makemigrations')
        print('migrate')
        os.system('python manage.py migrate')
        print('users_generate')
        os.system('python manage.py user_groups_generate')
        print('user_groups_generate')
        os.system('python manage.py users_generate')
        print('subjects_generate')
        os.system('python manage.py subjects_generate')
        print('groups_generate')
        os.system('python manage.py groups_generate')
        print('attendances_generate')
        os.system('python manage.py attendances_generate')
        print('exams_generate')
        os.system('python manage.py exams_generate')
        print('payments_generate')
        os.system('python manage.py payments_generate')
        print('lessons_generate')
        os.system('python manage.py lessons_generate')
        os.system('python manage.py runserver')

