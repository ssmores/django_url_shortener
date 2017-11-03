from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.

# Function based view
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(KirrURL, shortcode=shortcode)

    # If you wanted a default to happen, use one of the following below.
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()


    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    
    return HttpResponse('hello {sc}'.format(sc=obj.url))


# Class based view
class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)  
        return HttpResponse()

    def post(self, request, *args, **kwargs):
        return HttpResponse()
