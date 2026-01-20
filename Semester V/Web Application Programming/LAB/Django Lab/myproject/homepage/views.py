from django.shortcuts import render
from homepage.models import item

# Create your views here.

def index(request):
    data = item.objects.all()
   

    return render(request , 'homepage/index.html',context= {'data' : data})

def contacts(request):
    context = {
        'data' : ["a","b","c","d"]
    }
    return render(request , 'homepage/contacts.html',context=context)


