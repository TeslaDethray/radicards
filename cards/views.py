from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from cards.models import Art, Artist, Card, Template
from constance import config
from django.views import generic
from PIL import Image, ImageDraw, ImageFont
import settings
import hashlib
import os

def add(request):
    card = Card.create(request)
    url = '/card/' + card.slug
    return HttpResponseRedirect(url)

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
    model = Artist
    template_name = config.TEMPLATE + '/index_artist.html'

    def get_queryset(self):
        return Artist.objects.order_by('last_name')

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
    image_name = request.GET.get('template') + '+' + request.GET.get('text')
    hash_object = hashlib.md5(str(image_name).encode())
    card_location = settings.MEDIA_ROOT + "/cards/" + hash_object.hexdigest() + ".jpg"

    #Check to see if this image already exists
    if not os.path.exists(card_location): 
        template = Template.objects.get(pk = request.GET.get('template'))
        font = ImageFont.truetype(str(template.font.font_file), int(template.font_size))
        im1 = Image.open(str(template.art.image))

        # Drawing the text on the picture
        draw = ImageDraw.Draw(im1)
        draw.text((template.x_coord, template.y_coord), request.GET.get('text'), template.text_color, font = font)
        draw = ImageDraw.Draw(im1)

        # Save the image with a new name
        im1.save(card_location)

    return HttpResponse('<img src="' + settings.MEDIA_URL + 'cards/' + hash_object.hexdigest() + '.jpg"><input type="hidden" name="hash" value="' + hash_object.hexdigest() + '">')

def view(request, slug):
    try:
        card = Card.objects.get(slug = slug)
    except Card.DoesNotExist:
        raise Http404
    return render(request, config.TEMPLATE + '/view.html', {'card': card, 'url': request.build_absolute_uri(), 'media_url': settings.MEDIA_URL, 'config': config})

