from django.conf import settings
from django_hosts import patterns, host 

host_patterns = patterns('', 
    host(r'www', settings.ROOT_URLCONF, name='www'), 
    #host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
    host(r'(?!www).*', 'kirr.urls', name='wildcard'),
    )


# This may be a future implementation/way to do this url redirecting.
'''
from kirr.hostsconf import urls as redirect_urls

host_patterns =  [
    host(r'www', settings.ROOT_URLCONF, name='www'), 
    host(r'(?!www).*', redirect_urls, name='wildcard'),
    ]
'''