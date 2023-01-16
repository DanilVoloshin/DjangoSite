from django.urls import path
 
from .views import order_table

 
urlpatterns = [
    path('', order_table, name='home'),
    
]