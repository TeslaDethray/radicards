from django.db import models
from collections import defaultdict
from constance import config
from paintstore.fields import ColorPickerField
import settings
import os
import hashlib

class Artist(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    biography = models.TextField(blank = True)
    image = models.ImageField(upload_to = os.path.join(settings.BASE_DIR, 'media/artist'), blank = True)
    url = models.CharField(max_length = 144, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def image_name(self):
        return settings.MEDIA_URL + 'artist/' + str(self.image).split('/')[-1]

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def __unicode__(self): #Python 2.x
        return self.first_name + ' ' + self.last_name

class Art(models.Model):
    name = models.CharField(max_length = 89)
    artist = models.ForeignKey(Artist, null = True, blank = True)
    image = models.ImageField(upload_to = os.path.join(settings.BASE_DIR, 'media/art'))
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def image_name(self):
        return settings.MEDIA_URL + 'art/' + str(self.image).split('/')[-1]

    class Meta:
        verbose_name_plural = 'art'
    def __str__(self):
        return self.name
    def __unicode__(self): #Python 2.x
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length = 55, blank = True)
    last_name = models.CharField(max_length = 55, blank = True)
    email = models.CharField(max_length = 89, blank = True)
    postal_code = models.CharField(max_length = 13, blank = True)
    mailing_list = models.BooleanField(default = False)
    referrer = models.CharField(max_length = 55, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    @classmethod
    def create_or_update(cls, data, who):
        try:
            person = Person.objects.get(email = data['email'])
        except Person.DoesNotExist:
            person = Person()
        if 'sender' in who:
            person.referrer = data['referrer']
            person.mailing_list = data['mailing_list']
            person.postal_code = data['postal_code']
        person.first_name = data['first_name']
        person.last_name = data['last_name']
        person.email = data['email']
        person.save()
        return person

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def __unicode__(self): #Python 2.x
        return self.first_name + ' ' + self.last_name

class Font(models.Model):
    name = models.CharField(max_length = 34)
    font_file = models.FileField(upload_to = os.path.join(settings.BASE_DIR, 'media/fonts'), null = True, blank = True)

    def __str__(self):
        return self.name
    def __unicode__(self): #Python 2.x
        return self.name

class Template(models.Model):
    art = models.ForeignKey(Art)
    order = models.IntegerField(default = 0)
    x_coord = models.IntegerField(default = 0)
    y_coord = models.IntegerField(default = 0)
    max_width = models.IntegerField(default = 0)
    max_height = models.IntegerField(default = 0)
    text_color = ColorPickerField()
    font = models.ForeignKey(Font)
    font_size = models.CharField(max_length = 8)
    published = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def image(self):
        image_location = str(self.art.image)
        return '/' + image_location.replace(settings.BASE_DIR, '')
    def artist(self):
        return self.art.artist
    def form_fields(self, string_fields):
        fields = string_fields.replace(' ', '').split(',')

        field_dict = {
            'sender': [],
            'recipient': [],
            'message': [],
        }

        for field in fields:
            field_split = field.split('_', 1)
            attribute = field_split.pop()
            if not field_split:
                field_dict[attribute] = True
            else:
                part = field_split.pop()
                field_dict[part].append(attribute)

        return field_dict

    def field_types(self):
        field_types = {
            'first_name': 'text', 
            'last_name': 'text', 
            'email': 'text', 
            'postal_code': 'text', 
            'referrer': 'hidden', 
            'mailing_list': 'checkbox', 
            'message': 'textarea', 
        }
        return field_types

    def field_labels(self):
        field_types = {
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'email': 'Email', 
            'postal_code': 'Postal Code', 
            'mailing_list': 'Join Our Mailing List?', 
            'message': 'Message', 
        }
        return field_types

    def __str__(self):
        return self.art.name
    def __unicode__(self): #Python 2.x
        return self.art.name

class Card(models.Model):
    template = models.ForeignKey(Template, null = True)
    recipient = models.ForeignKey(Person, related_name = '+', null = True)
    sender = models.ForeignKey(Person, related_name = '+', null = True)
    slug = models.SlugField(max_length = 55)
    hashed_id = models.SlugField(max_length = 55, null = True)
    short_url = models.CharField(max_length = 55, null = True)
    message = models.TextField(null = True, blank = True)
    featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    @classmethod
    def create(cls, request):
        sender_data = {'first_name': '', 'last_name': '', 'email': '', 'postal_code': '', 'mailing_list': False, 'referrer': ''}
        recipient_data = {'first_name': '', 'last_name': '', 'email': '', 'postal_code': '', 'mailing_list': False, 'referrer': ''}
        message = ''
        for field in request.POST:
            if 'sender_' in field:
                field_name = field.replace('sender_', '')
                sender_data[field_name] = request.POST.get(field)
            if 'recipient_' in field:
                field_name = field.replace('recipient_', '')
                recipient_data[field_name] = request.POST.get(field)
            if 'message' in field:
                message = request.POST.get(field)
        sender = Person.create_or_update(sender_data, 'sender')
        recipient = Person.create_or_update(recipient_data, 'recipient')

        card = Card()
        card.message = message 
        card.template = Template.objects.get(pk = request.POST.get('template'))
        card.hashed_id = request.POST.get('hash')
        card.sender = sender
        card.recipient = recipient
        card.save()
        hash_object = hashlib.md5(str(card.id).encode())
        card.slug = hash_object.hexdigest()
        card.save()
        return card
    
    def featured_cards(self):
        try:
            return Card.objects.get(featured=True)
        except Card.DoesNotExist:
            return False

    def __str__(self):
        return self.slug
    def __unicode__(self): #Python 2.x
        return self.slug

