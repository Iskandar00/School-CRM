import datetime

from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter
def datetime_to_minute(created_at):
    if type(created_at)!=datetime.datetime:
        return 'No message yet'
    current_datetime = now() - created_at
    seconds = int(current_datetime.total_seconds())

    if seconds < 60:
        return f'{seconds} seconds'

    minutes = seconds // 60
    if minutes < 60:
        return f'{minutes} minutes'

    hours = minutes // 60
    if hours < 24:
        return f'{hours} hours'

    days = hours // 24
    if days < 7:
        return f'{days} days'

    weeks = days // 7

    return f'{weeks} weeks'
