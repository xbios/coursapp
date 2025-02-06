
from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_view),
    path('anasayfa', views.my_view),
    path('kurslar', views.kurslar),
    
]
