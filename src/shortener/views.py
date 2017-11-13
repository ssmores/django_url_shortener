from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        print 'in the homeview get method'
        form = SubmitUrlForm()
        context = {
            "title": "Kirr.co",
            "form": form,
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        print 'in the homeview post method'
        form = SubmitUrlForm(request.POST)

        context = {
            "title": "Kirr.co",
            "form": form,
        }
        template = "shortener/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj, 
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)


# Class based view
class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print 'in kirrcbview method'
        obj = get_object_or_404(KirrURL, shortcode=shortcode)  
        return HttpResponseRedirect(obj.url)

