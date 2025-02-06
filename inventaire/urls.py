from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('addreservation/',addreservation,name='addreservation'),
    path('reservations/',reservations,name='reservations'),
    path('reservations/<str:ref>',deleteReservation,name='deleteReservation'),
    path('stock/',stock,name='stock'),
    path('detailStock/<str:ref>',detailStock,name='detailStock'),
    path('addstock/',addStock,name='addstock'),

]
