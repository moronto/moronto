from rest_framework import serializers

from inventaire.models import Stock,GroupeElectrogene,CabinesAutonome,Modulaire

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields=['refMateriel','designation','situation','lieu','client','categorie']

class GroupeElectrogeneSerializer(serializers.ModelSerializer) :
    class Meta:
        model=GroupeElectrogene
        fields='__all__'       

class CabinesAutonomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CabinesAutonome
        fields='__all__'

class ModulaireSerializer(serializers.ModelSerializer):
    class Meta:
        model=Modulaire
        fields='__all__'
