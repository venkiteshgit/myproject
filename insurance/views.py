from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Insured

def index(request):
    insured_details = Insured.objects.all()
    template = loader.get_template('insurance/index.html')
    context = {
        'insured_details': insured_details,
    }
    return HttpResponse(template.render(context, request))
    #output = ', '.join([q.first_name for q in firstrecord])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the insurance  index.")
# Create your views here.
