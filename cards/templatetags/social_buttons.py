from django import template
from django.template.base import Node
from constance import config

register = template.Library()

class SocialMediaButtons(Node):
    def render(self, context):
        return config.SHARE
