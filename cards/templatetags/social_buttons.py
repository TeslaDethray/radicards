from django import template
from django.template.base import Node
from urlparse import urlparse
from constance import config

register = template.Library()

def facebook(url):
    return '<a href="https://facebook.com/sharer/sharer.php?u=' + url + '"><img src="/static/forestethics/images/fe-fb.png" border=0 alt="Facebook"></a>'

def twitter(url, role):
    status = {
        'sender': "Send Love, Save Forests",
        'recipient': "<3 this beautiful card!",
        'default': "Send a message of <3, forests %26 @ForestEthics",
    }
    return '<a href="https://twitter.com/home?status=' + status[role] + " " + url + '"><img src="/static/forestethics/images/fe-tw.png" border=0 alt="Twitter"</a>'

def google(url):
    return '<a href="https://plus.google.com/share?url=' + url + '"><img src="/static/forestethics/images/fe-gp.png" border=0 alt="Google+"</a>'

def tumblr(url):
    return '<a href="http://www.tumblr.com/share/link?url=' + url + '"><i class="icon-large icon-tumblr"> </i></a>'

def linkedin(url):
    return '<a href="https://www.linkedin.com/shareArticle?mini=true&title=&summary=&source=&url=' + url + '"><i class="icon-large icon-linked-in"> </i></a>'

def pinterest(url):
    return '<a href="https://pinterest.com/pin/create/button/?url=&description=&media=' + url + '"><i class="icon-large icon-pinterest"> </i></a>'

@register.filter
def render(self, url):
    role = 'recipient'
    if 'new' in url:
        role = 'sender'
    if 'share' in url:
        role = 'default'

    url = url.replace('?new=1', '').replace('?share=1', '')
    url += '?share=1'
    buttons = {
        'facebook': facebook(url),
        'twitter': twitter(url, role),
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
