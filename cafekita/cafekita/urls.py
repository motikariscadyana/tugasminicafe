from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatteres = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('api-auth/', include('rest_framework.urls'))

]