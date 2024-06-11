# Generated by Django 5.0.6 on 2024-06-10 07:56

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('week_days', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(choices=[(0, 'monday'), (1, 'tuesday'), (2, 'wednesday'), (3, 'thursday'), (4, 'friday'), (5, 'saturday'), (6, 'sunday')]), size=None)),
                ('create_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subject_groups', to='subjects.subject')),
            ],
        ),
    ]