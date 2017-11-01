from __future__ import unicode_literals
import random 
import string
from django.db import models

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(char)
    # return new_code

    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)


    def save(self, *args, **kwargs):
        """Overwriting existing save method to take args and kwargs."""
        print 'something'
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)





    def __str__(self):
        return str(self.url)


    def __unicode__(self):
        return str(self.url)
