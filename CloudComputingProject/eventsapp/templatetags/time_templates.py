from django.utils import timezone as tz
from django import template
register = template.Library()

@register.simple_tag
def get_now():
    return tz.now()

