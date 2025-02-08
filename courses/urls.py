
from django.urls import path
from . import views


urlpatterns = [    
    path('', views.index),     
    path('<kurs_adi>', views.details),        
    path('kategory/<int:category_id>', views.getcoursesByCategoryId),    
    path('kategory/<str:category_name>', views.getcoursesByCategory,name='courses_by_category'),
]
