from django.core.management import BaseCommand
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        CustomUser.objects.create_superuser(role=CustomUser.RoleChoices.Admin.value,
                                            password='1',
                                            first_name='Iskandar',
                                            last_name='Diyorov',
                                            gender='male',
                                            father_name='O\'ktam o\'g\'li',
                                            phone_number='+998908897414',
                                            email=f'diyor1ov2@gmail.com',
                                            address='Olmazor')

        CustomUser.objects.create_user(role='teacher',
                                       password='3',
                                       first_name='Oy bola',
                                       last_name='Oyev',
                                       gender='male',
                                       salary=f'{1000}',
                                       father_name='Tomir bobo',
                                       phone_number='+998911234667',
                                       email='c1@c.cc',
                                       address='Yunusobod'),

        self.stdout.write(self.style.SUCCESS('admin and teacher created'))
