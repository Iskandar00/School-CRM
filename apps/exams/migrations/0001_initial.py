# Generated by Django 5.0.6 on 2024-06-13 08:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.PositiveSmallIntegerField()),
                ('limit_hour', models.PositiveSmallIntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subjects.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.PositiveSmallIntegerField()),
                ('comment', models.TextField(blank=True, max_length=2000)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='exams.exam')),
            ],
        ),
    ]
