from django.shortcuts import render
from .models import *

def newLivraison(request):
    if request.method=='POST':
        req=request.POST
        bl=Livraison(
            
            client=request.POST.get("client"),
            dateLivraison='2025-02-02',#request.POST.get("dateLivraison"),
            refMateriel=request.POST.getlist("refMateriel"),
            designation=request.POST.getlist("designation"),
            qte=request.POST.getlist("qte"),
            observations=request.POST.getlist("observation"),
            chargerAffaire=request.POST.get("chargerAffaire"),
            typeLivraison=request.POST.get("typeLivraison"),
            chantier=request.POST.get("chantier"),
            typeTrans=request.POST.get("typeTans"),
            matTrans=request.POST.get("matTans"),
            condTrans=request.POST.get("condTrans"),

        )
        bl.save()
           
    


    return render(request,'livraisons/newLivraison.html')
