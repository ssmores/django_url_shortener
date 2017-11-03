from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

# Function based view
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    print shortcode
    return HttpResponse('hello') 


# Class based view
class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):

        print shortcode
        return HttpResponse()