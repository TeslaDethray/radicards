from django.db import models
from paintstore.fields import ColorPickerField

class Artist(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    biography = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'media/artist', blank = True)
    url = models.CharField(max_length = 144, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def __unicode__(self): #Python 2.x
        return self.first_name + ' ' + self.last_name

class Art(models.Model):
    name = models.CharField(max_length = 89)
    artist = models.ForeignKey(Artist, null = True, blank = True)
    image = models.ImageField(upload_to = 'media/art')
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        verbose_name_plural = 'art'
    def __str__(self):
        return self.name
    def __unicode__(self): #Python 2.x
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55, blank = True)
    email = models.CharField(max_length = 89, blank = True)
    postal_code = models.CharField(max_length = 13, blank = True)
    mailing_list = models.BooleanField(default = False)
    referrer = models.CharField(max_length = 55, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    def __unicode__(self): #Python 2.x
        return self.first_name + ' ' + self.last_name

class Font(models.Model):
    name = models.CharField(max_length = 34)
    font_file = models.FileField(upload_to = 'media/fonts', null = True, blank = True)
    external_url = models.CharField(max_length = 144, null = True, blank = True)

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

    def artist(self):
        return self.art.artist

    def __str__(self):
        return self.art.name
    def __unicode__(self): #Python 2.x
        return self.art.name

class Card(models.Model):
    template = models.ForeignKey(Template, null = True)
    recipient = models.ForeignKey(Person, related_name = '+', null = True)
    sender = models.ForeignKey(Person, related_name = '+', null = True)
    slug = models.SlugField(max_length = 55)
    short_url = models.CharField(max_length = 55, null = True)
    message = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    def __str__(self):
        return self.slug
    def __unicode__(self): #Python 2.x
        return self.slug
