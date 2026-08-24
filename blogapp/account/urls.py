from django.urls import path
from . import views

urlpatterns = [
    path('Giriş', views.giriş_request, name='Giriş'),
    path('Kayıt', views.kayıt_request, name='Kayıt'),
    path('Çıkış', views.çıkış_request, name='Çıkış'),
]
