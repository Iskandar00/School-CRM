from django.core.validators import MinValueValidator
from django.db import models


class Subject(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)],
                                help_text="add in UZS")
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True)
    published_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, related_name='resource')
    author = models.CharField(max_length=75, blank=True)
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    month = models.PositiveSmallIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject}: {self.name}'
