from django.shortcuts import render
from django.template import RequestContext, loader

# Create your views here.
def contact(request):
    context = {}
    return render(request, 'contact.html', context)