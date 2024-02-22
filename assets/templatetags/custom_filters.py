# custom_filters.py

from django import template

register = template.Library()


@register.filter(name="replace_underscores")
def replace_underscores(value):
    return value.replace("_", " ")
