from django.contrib import admin
from django.urls import path   

from . import views 

urlpatteres = [
    path('admin/', admin.site.urls),
    path('', views.index),

]