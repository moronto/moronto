from django.shortcuts import render
from .models import *
import json
def home(request):
    return render(request,'inventaire/home.html')

def login(request):
    return render(request,'inventaire/login.html')


def reservations(request):

    if request.method=='POST':
   
        d=dict(request.POST)
        
        g=list(d.items())
        c=dict(g[5:])
        e=g[5:]
        print(len(e))
        for i in e:
            print(i[1])
    
    


    return render(request,'inventaire/reservations.html')