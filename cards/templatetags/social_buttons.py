from django import template
from django.template.base import Node
from constance import config

register = template.Library()

@register.filter
def render(self, context):
    return config.SHARE
