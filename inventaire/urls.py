from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('reservations/',reservations,name='reservations'),
    path('stock/',stock,name='stock'),
    path('detailStock/<str:ref>',detailStock,name='detailStock'),

]
