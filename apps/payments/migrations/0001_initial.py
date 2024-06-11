# Generated by Django 5.0.6 on 2024-06-10 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(default=2024, validators=[django.core.validators.MinValueValidator(2005), django.core.validators.MaxValueValidator(2025)])),
                ('month', models.PositiveSmallIntegerField(choices=[(1, 'january'), (2, 'february'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('in_percent', models.PositiveSmallIntegerField(default=100)),
            ],
        ),
    ]