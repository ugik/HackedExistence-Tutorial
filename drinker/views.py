from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm

def DrinkerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        pass
    else:
        ''' user is not submitting the form '''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))
