from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    context = {}
    return render(request, 'index.html', context)