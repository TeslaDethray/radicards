from django.contrib import admin
from settings.models import *

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('option', 'value')

admin.site.register(Settings, SettingsAdmin)
