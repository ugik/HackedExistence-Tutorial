from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^beers/$', 'beer.views.BeersAll'),
    (r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer'),
    (r'^brewerys/(?P<breweryslug>.*)/$', 'beer.views.SpecificBrewery'),
)

