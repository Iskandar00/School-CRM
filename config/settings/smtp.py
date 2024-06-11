import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER'],
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'],
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
