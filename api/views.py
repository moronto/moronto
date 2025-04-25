from django.shortcuts import render, get_object_or_404
from rest_framework import status
from api.serializers import *
from inventaire.models import Stock
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse




class StockData(ModelViewSet):
    queryset=Stock.objects.all().order_by('-created_at')
    serializer_class=StockSerializer

@api_view(['GET'])
def detailStock(request, ref):
    data=[]
    try:
        mat = get_object_or_404(Stock, refMateriel=ref)
        serializer = StockSerializer(mat)
        data.append(serializer.data)
        
        if serializer.data['categorie']=="GROUPE ELECTROGENE":
            GE=get_object_or_404(GroupeElectrogene, refMateriel=ref)
            serializerGE=GroupeElectrogeneSerializer(GE)
            data.append(serializerGE.data)
        elif serializer.data['categorie']=="MODULAIRE":
            MOD=get_object_or_404(Modulaire,refMateriel=ref)
            serializerMOD=ModulaireSerializer(MOD)
            data.append(serializerMOD.data)
        elif serializer.data['categorie']=="CABINES AUTONOMES":
            CAB=get_object_or_404(CabinesAutonome,refMateriel=ref)
            serializerCAB=CabinesAutonomeSerializer(CAB)
            data.append(serializerCAB.data)
                
        
        return Response({
            'status': 'success',
            'data': data
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
@api_view(['POST','GET'])
def addStock(request):
    data={}
    
    if request.method == 'POST':

        data=request.data
        st=Stock.objects.get_or_create(
        refMateriel=data.get('refMateriel'),
        designation=data.get('designation'),
        situation="DISPONIBLE",
        lieu=data.get('lieu'),
        categorie=data.get('categorie'),
        )
        

        print(data.get('dimension'))

        if data.get('categorie')=='GROUPE ELECTROGENE':
            print('hayi')
            GE=GroupeElectrogene.objects.get_or_create(
                puissance=data.get('puissance'),
                marque=data.get('marque'),
                dimension=data.get('dimension'),
                refMateriel=st[0],
            )
            
        elif  data.get('categorie')=='MODULAIRE':
            MOD=Modulaire.objects.get_or_create(
                gamme=data.get('gamme'),
                dimension=data.get('dimension'),
                refMateriel=st[0],
            )
            
        elif  data.get('categorie')=='CABINES AUTONOMES':
            CAB=CabinesAutonome.objects.get_or_create(
                gamme=data.get('gamme'),
                dimension=data.get('dimension'),
                color=data.get('color'),
                refMateriel=st[0],
            )
             


       

    return Response(data) 
       
@api_view(['DELETE'])
def deleteStock(request,ref):
    print('larefercen est', ref)
    try:
       stock=Stock.objects.get(refMateriel=ref)
    except Stock.DoesNotExist :
        return Response(
            {"erreur":"ce materiel n'existe pas"},
            status=status.HTTP_404_NOT_FOUND
        )  
    stock.delete()
    
    return Response(
        status=status.HTTP_200_OK
    )
    