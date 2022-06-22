from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name= 'index' ),
path('lnaddress/', views.lnaddress, name= 'lnaddress' ),
path('lninvoice/', views.lninvoice, name= 'lninvoice' ),
path('lnurl/', views.lnurl, name= 'lnurl' ),
]



