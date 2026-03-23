from django.contrib import admin
from django.urls import path
from members.views import member_list # On importe la vue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member_list, name='home'), # La page d'accueil affiche la liste
]