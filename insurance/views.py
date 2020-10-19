from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Insured
from django.views.decorators.csrf import requires_csrf_token

def index(request):
    return render(request, "insurance/index.html") 
    #return HttpResponse("Hello, world. You're at the insurance  index.")

def get_insured_details(request):
    insured_details = Insured.objects.all()
    template = loader.get_template('insurance/get_insured_details.html')
    context = {
        'insured_details': insured_details,
    }
    return HttpResponse(template.render(context, request))


def add_insured_details(request):
    return render(request, "insurance/add_insured_details.html") 

@requires_csrf_token
def submit_ensured_details(request):
    c = {}
    if request.method == 'POST':
        m_first_name = request.POST.get("first_name",default=None)
        m_last_name = request.POST.get("last_name",default=None)
        m_email = request.POST.get("email",default=None)
        m_phoneno = request.POST.get("phoneno",default=None)
        m_address1 = request.POST.get("address1",default=None)
        m_address2 = request.POST.get("address2",default=None)
        m_city = request.POST.get("city",default=None)
        m_country = request.POST.get("country",default=None)
        m_zip_code = request.POST.get("zip_code",default=None)
        m_dob = request.POST.get("dob",default=None)
        p = Insured(first_name=m_first_name,last_name=m_last_name,email=m_email,phone_number=m_phoneno,address1=m_address1,address2=m_address2,city=m_city,country=m_country,zip_code=m_zip_code,dob=m_dob)


        p.save()
        return render(request, "insurance/a_template.html", c)
    else:
        return render(request, "insurance/a_template.html", c)
    #output = ', '.join([q.first_name for q in firstrecord])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the insurance  index.")
# Create your views here.
