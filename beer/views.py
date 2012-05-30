from django.shortcuts import render_to_response
from django.template import RequestContext
from beer.models import Beer, Brewery

def BeersAll(request):
    beers = Beer.objects.all().order_by('name')
    context = {'beers': beers}
    return render_to_response('beersall.html', context, context_instance=RequestContext(request))
    
def SpecificBeer(request, beerslug):
    beer = Beer.objects.get(slug=beerslug)
    context = {'beer': beer}
    return render_to_response('singlebeer.html', context, context_instance=RequestContext(request))
    
def SpecificBrewery(request, breweryslug):
    brewery = Brewery.objects.get(slug=breweryslug)
    beers = Beer.objects.filter(brewery=brewery)
    context = {'beers': beers}
    return render_to_response('singlebrewery.html', context, context_instance=RequestContext(request))
