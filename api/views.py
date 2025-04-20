from django.shortcuts import render, get_object_or_404
from api.serializers import *
from inventaire.models import Stock
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status





class StockData(ModelViewSet):
    queryset=Stock.objects.all()
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



