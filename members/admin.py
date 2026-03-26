from django.contrib import admin
from .models import Member # Utilise .models car admin.py est dans le même dossier

class MemberAdmin(admin.ModelAdmin):
    # Les colonnes que tu verras dans la liste
    list_display = ('full_name', 'english_level', 'is_approved', 'created_at')
    
    # Un filtre sur le côté pour voir vite qui est approuvé
    list_filter = ('is_approved', 'english_level')

# On enregistre le modèle avec sa configuration personnalisée
admin.site.register(Member, MemberAdmin)