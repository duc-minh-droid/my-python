from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']

    member = Members(firstname=x, lastname=y)
    member.save()

    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
    

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']

    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

def testing(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers,
    }

    return HttpResponse(template.render(context, request))


def back(request):
    return HttpResponseRedirect(reverse('index'))

# get column
# def testing(request):
#   mydata = Members.objects.values_list('firstname')
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

# get row
# def testing(request):
#   mydata = Members.objects.filter(firstname='Emil').values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mydata,
#   }
#   return HttpResponse(template.render(context, request))

def moretest(request):
    template = loader.get_template('test3.html')
    first_member = Members.objects.all().values()[0]
    context = {
        'fir': first_member,
    }
    return HttpResponse(template.render(context, request))





