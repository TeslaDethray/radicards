from django import template
from django.template.base import Node
from urlparse import urlparse
from constance import config

register = template.Library()

def facebook(url):
    return '<a href="https://facebook.com/sharer/sharer.php?u=' + url + '"><i class="icon-large icon-facebook"> </i></a>'

def twitter(url):
    return '<a href="https://twitter.com/home?status==' + url + '"><i class="icon-large icon-twitter"> </i></a>'

def google(url):
    return '<a href="https://plus.google.com/share?url=' + url + '"><i class="icon-large icon-google-plus"> </i></a>'

def tumblr(url):
    return '<a href="http://www.tumblr.com/share/link?url=' + url + '"><i class="icon-large icon-tumblr"> </i></a>'

def linkedin(url):
    return '<a href="https://www.linkedin.com/shareArticle?mini=true&title=&summary=&source=&url=' + url + '"><i class="icon-large icon-linked-in"> </i></a>'

def pinterest(url):
    return '<a href="https://pinterest.com/pin/create/button/?url=&description=&media=' + url + '"><i class="icon-large icon-pinterest"> </i></a>'

@register.filter
def render(self, url):
    buttons = {
        'facebook': facebook(url),
        'twitter': twitter(url),
        'google+': google(url),
        'tumblr': tumblr(url),
        'pinterest': pinterest(url),
        'linkedin': linkedin(url),
    }

    shares = config.SHARE.split(',')
    html = []
    for share in shares:
        html.append('<span class="share-button ' + share.strip().lower() + '">' + buttons[share.strip().lower()] + '</span>')

    return ' '.join(html)
