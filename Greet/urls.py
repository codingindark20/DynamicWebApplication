from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('vat',views.vat, name='vat')
]