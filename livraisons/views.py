from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from inventaire.models import *
from datetime import timezone,datetime
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse


def livraison(request):
    
    data=Livraison.objects.all()
    # if request.method=='POST':
    return render(request,'livraisons/livraison.html',{
            'title':'Livraisons',
            'livraisonData':data
            
            })

def newLivraison(request):
    if request.method=='POST':
        req=request.POST
        currentYear=datetime.now().strftime("%Y").strip()
        bls=[]
        livraison=Livraison.objects.all()
        if livraison.count() != 0:
            for r in livraison:
                bls.append(int(r.bl.split('-')[0]))
            bl=f'{str((max(bls)+1)).zfill(4)}-{currentYear}'
        else:    
            bl=f'0001-{currentYear}'

        bl=Livraison(
            bl=bl,
            client=request.POST.get("client"),
            dateLivraison=request.POST.get("dateLivraison"),
            chargerAffaire=request.POST.get("chargerAffaire"),
            typeLivraison=request.POST.get("typeLivraison"),
            chantier=request.POST.get("chantier"),
            created_by=request.user.username,
           
        )
        bl.save()
        
  
     
        
        l=len(req.getlist("refMateriel"))
       
        for i in range(l):
            print(i)
            detail=DetailsLivraison(
                bl=bl,
                refMateriel=req.getlist('refMateriel')[i],
                designation=req.getlist('designation')[i],
                qte=int(req.getlist('qte')[i]),
                matTrans=req.getlist("matTrans")[i],
                condTrans=req.getlist("condTrans")[i],
                observations=req.getlist('observations')[i],
            )
            detail.save()
        messages.success(request,f'Vous avez ajouter BL N° {bl} avec succes')
        return redirect('livraison')
        
    

    return render(request,'livraisons/newLivraison.html',{
        'title':'Ajouter nouveau',
        'charger':Chargesaffaire.objects.all(),
        'client':['SOGEA','NGE','TGCC','AVANT SCENE','ACWA POWER','SENER']
    })


def designation(request):
    ref=request.GET.get('valSearch')
    data=Stock.objects.filter(refMateriel=ref).values('designation')
    if len(data)==0:
        d={'designation':""}
    else:
        d=data[0]    

    return JsonResponse({'data':d})
def detailsLivraison(request,bl):
    detail=Livraison.objects.filter(bl=bl).values()[0]
    detailMat=DetailsLivraison.objects.filter(bl=bl).values()

    return render(request,'livraisons/detailsLivraison.html',{
        'title':f'Details de {bl}',
        'detail':detail,
        'detailMat':detailMat,
         
    })



