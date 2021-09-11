from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('travels', views.travels),
    path('view', views.view),
    path('addtrip', views.addtrip),
    path('registro', auth.registro),
    path('login', auth.login),
    path('logout', auth.logout)
]
