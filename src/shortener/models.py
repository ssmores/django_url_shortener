from __future__ import unicode_literals
from django.db import models
from .utils import code_generator, create_shortcode


# Create your models here.

#Model managers
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    #Change all codes at the same time
    def refresh_shortcodes(self):
        qs = KirrURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print q.shortcode
            q.save()
            new_codes += 1
        return 'New codes made: {i}'.format(i=new_codes)


class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    objects = KirrURLManager()


    def save(self, *args, **kwargs):
        """Overwriting existing save method to take args and kwargs."""
        if not self.shortcode:
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)





    def __str__(self):
        return str(self.url)


    def __unicode__(self):
        return str(self.url)
