from django.urls import path
from global1 import views

urlpatterns = [
    path('global1/',views.global1,name='global1'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('help/',views.help,name='help'),
    path('services/',views.services,name='services'),
    path('form/',views.form,name='form'),
 ]
