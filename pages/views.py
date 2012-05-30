from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import HomePage

def MainHomePage(request):
    homepage = HomePage.objects.get(pk=1)
    context = {'homepage': homepage}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
