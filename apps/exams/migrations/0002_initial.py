# Generated by Django 5.0.6 on 2024-06-24 21:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='examresult',
            name='student',
            field=models.ForeignKey(limit_choices_to={'role': 'student'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='exam',
            unique_together={('subject', 'month')},
        ),
        migrations.AlterUniqueTogether(
            name='examresult',
            unique_together={('student', 'exam')},
        ),
    ]
