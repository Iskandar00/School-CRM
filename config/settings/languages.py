import os
from django.conf import settings

LANGUAGE_CODE = 'uz'
LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    ('uz', 'Uzbek'),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'en', 'ru')
USE_I18N = True
