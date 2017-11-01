from __future__ import unicode_literals
from django.db import models
from .utils import code_generator, create_shortcode


# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        """Overwriting existing save method to take args and kwargs."""
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)





    def __str__(self):
        return str(self.url)


    def __unicode__(self):
        return str(self.url)
