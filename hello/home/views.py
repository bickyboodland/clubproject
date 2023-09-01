from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        motive = request.POST.get('motive')
        contact_obj = Contact(name=name,email=email,phone=phone,motive=motive,date = datetime.today())
        contact_obj.save()
        messages.success(request,'Your message has been sent')
    return render(request, 'contact.html')
