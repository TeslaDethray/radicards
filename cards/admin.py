from django.contrib import admin
from cards.models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'template', 'created_at')
    list_display_links = None

    def has_add_permission(self, request):
        return False
    def has_edit_permission(self, request):
        return False

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'referrer', 'mailing_list')
    list_editable = ['mailing_list']
    list_display_links = None

    def has_add_permission(self, request):
        return False

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'art', 'artist')

admin.site.register(Art, ArtAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Font)
admin.site.register(Person, PersonAdmin)
admin.site.register(Template, TemplateAdmin)
