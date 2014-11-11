from django.contrib import admin
from cards.models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'template', 'created_at')
    fields = ['template', 'recipient', 'sender', 'message']

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'referrer', 'mailing_list')

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'art', 'artist')

admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Template, TemplateAdmin)
