from django.contrib import admin
from .models import Member

# On dit à l'admin d'afficher les membres
admin.site.register(Member)