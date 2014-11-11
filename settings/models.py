from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length = 55)
    option = models.CharField(max_length = 144, blank = True, null = True)
    help_text = models.TextField(blank = True, null = True)
    value = models.TextField(blank = True, null = True)
    options = models.TextField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)

    class Meta:
        verbose_name_plural = 'settings'
    def __str__(self):
        return self.name
    def __unicode__(self): #Python 2.x
        return self.name
