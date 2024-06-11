# Generated by Django 5.0.6 on 2024-06-10 07:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, help_text='add in UZS', max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=75, unique=True)),
                ('published_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=75)),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('published_at', models.DateField(blank=True, null=True)),
                ('month', models.PositiveSmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='resource', to='subjects.subject')),
            ],
        ),
    ]
