from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

#Home
def home(request):
  return render_to_response("home.html", None, context_instance=RequestContext(request))