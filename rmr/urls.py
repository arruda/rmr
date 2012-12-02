from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic.simple import direct_to_template

from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^', include('accounts.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^books/', include('books.urls')),
     url(r'^authors/', include('authors.urls')),
     url(r'^publishers/', include('publishers.urls')),
     url(r'^stores/', include('stores.urls')),
     url(r'^faqs/$', direct_to_template, {'template': 'faqs.html'}, name='faqs'),
)


urlpatterns += patterns('django.contrib.auth.views',               

    url(r'^login/$', 'login', {'template_name': 'users/login.html',}, name='login'),  
    url(r'^logout/$', 'logout', {'template_name': 'users/login.html'},name='logout'),
        

)

if settings.SERVE_MEDIA:
    
    urlpatterns += staticfiles_urlpatterns()
