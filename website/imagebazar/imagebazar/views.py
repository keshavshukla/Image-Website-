from django.core.files import images
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *

def show_about_page(request):
    return render(request,'about.html',{})

def show_home_page(request):
    cats=Category.objects.all()

    images=Image.objects.all()
    data={'images': images,'cats':cats}
    return render(request,'home.html', data)

def show_category_page(request,cid):
    print(cid)
    cats=Category.objects.all()

    catog=Category.objects.get(pk=cid)

    images=Image.objects.filter(cat=catog)
    data={'images': images,'cats': cats}
    return render(request,'home.html', data)