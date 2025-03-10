from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('livraison/',livraison,name='livraison'),
    path('newlivraison/',newLivraison,name='newLivraison'),
    path('designation/',designation,name='designation'),
    path('detailsLivraison/<str:bl>',detailsLivraison,name='detailsLivraison'),

  
]