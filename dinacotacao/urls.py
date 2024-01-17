from django.urls import path, include
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.sites.urls),
    path('', include('dinacotacao.urls'))

]