from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
import os
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')}),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^beers/$', 'beer.views.BeersAll'),
    (r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer'),
    (r'^brewerys/(?P<breweryslug>.*)/$', 'beer.views.SpecificBrewery'),
    (r'^register/$', 'drinker.views.DrinkerRegistration'),
    (r'^login/$', 'drinker.views.LoginRequest'),
    (r'^logout/$', 'drinker.views.LogoutRequest'),
    (r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]*)-(?P<token>.*)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^direct/$', direct_to_template, {'template': 'direct.html', 'extra_context': {'showDirect': True}}),
    (r'^profile/$', 'drinker.views.Profile'),
)


