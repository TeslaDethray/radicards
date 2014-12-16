from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.utils.safestring import mark_safe
from subprocess import call
from cards.models import Art, Artist, Card, Template
from constance import config
from django.views import generic
from PIL import Image, ImageDraw, ImageFont
import settings
import hashlib
import os

def add(request):
    card = Card.create(request)
    url = reverse('view', kwargs = {'slug': card.slug}) + '?new=1'
    sender_subject = add_replace(card, config.EMAIL_SUBJECT_SENDER)
    sender_body = add_replace(card, config.EMAIL_BODY_SENDER)
    recipient_subject = add_replace(card, config.EMAIL_SUBJECT)
    recipient_body = add_replace(card, config.EMAIL_BODY)

    send_mail(recipient_subject, mark_safe(recipient_body), card.sender.email, [card.recipient.email], fail_silently = False)
    send_mail(sender_subject, mark_safe(sender_body), card.sender.email, [card.sender.email], fail_silently = False)
    return HttpResponseRedirect(url)

def add_replace(card, haystack):
    replace_fields = {
        'sender_first_name': card.sender.first_name,
        'recipient_first_name': card.recipient.first_name,
        'url': 'http://' + settings.DOMAIN + '/cards/' + card.slug,
        'image': 'http://' + settings.DOMAIN + settings.MEDIA_URL + 'cards/' + card.slug + '.jpg',
    }
    for needle in replace_fields.keys():
        haystack = haystack.replace('{{'+needle+'}}', replace_fields[needle])
    return haystack

def artist(request, artist_id):
    try:
        artist = Artist.objects.get(pk = artist_id)
    except Card.DoesNotExist:
        raise Http404
    art = Art.objects.filter(artist_id = artist_id)
    art_ids = []
    for art_piece in art:
        art_ids.append(art_piece.id)
    templates = Template.objects.filter(pk__in = art_ids)
    return render(request, config.TEMPLATE + '/artist.html', {'artist': artist, 'templates': templates})

class IndexArtistView(generic.ListView):
    model = Template
    template_name = config.TEMPLATE + '/index_artist.html'

    def get_queryset(self):
        return Template.objects.order_by('order')

def create(request, template_id):
    try:
        template = Template.objects.get(pk = template_id)
    except Template.DoesNotExist:
        raise Http404
    fields = config.FORM_FIELDS.split(',')
    return render(request, config.TEMPLATE + '/create.html', {'template': template, 'fields': template.form_fields(config.FORM_FIELDS), 'required': template.form_fields(config.REQUIRED_FIELDS), 'types': template.field_types, 'labels': template.field_labels})

class IndexView(generic.ListView):
    model = Template
    template_name = config.TEMPLATE + '/index.html'

    def get_queryset(self):
        return Template.objects.order_by('order')[:config.NUM_CARDS]

def image(request): #Presses text to image
    #Hashing the image name
    message = str(request.GET.get('message'))
    if message == 'None':
        message = ''
    
    image_name = str(request.GET.get('template')) + '+' + message
    hash_object = hashlib.md5(str(image_name).encode())
    card_location = settings.MEDIA_ROOT + "/cards/" + hash_object.hexdigest() + ".jpg"

    #Check to see if this image already exists
    if not os.path.exists(card_location): 
	command = 'php /home/radicaldesigns/radicards/cards/templates/forestethics/image.php ' + str(request.GET.get('template')) + ' ' + hash_object.hexdigest() + " '" + message + "'"
	call(command, shell = True)

    return HttpResponse('<img src="' + settings.MEDIA_URL + 'cards/' + hash_object.hexdigest() + '.jpg"><input type="hidden" name="hash" value="' + hash_object.hexdigest() + '" template="' + str(request.GET.get('template')) + '" text="' + message + '">')

def view(request, slug):
    try:
        card = Card.objects.get(slug = slug)
    except Card.DoesNotExist:
        raise Http404

    new = False
    if request.GET.get('new'):
        new = True

    return render(request, config.TEMPLATE + '/view.html', {'card': card, 'url': request.build_absolute_uri(), 'media_url': settings.MEDIA_URL, 'config': config, 'new': new,})
