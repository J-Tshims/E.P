from django.db import models

class Member(models.Model):
    # Les choix pour le niveau d'anglais
    LEVEL_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    english_level = models.CharField(max_length=3, choices=LEVEL_CHOICES, default='BEG')
    
    # LA CASE MAGIQUE : Par défaut, personne n'est approuvé (False)
    is_approved = models.BooleanField(default=False)
    
    # Pour savoir quand ils ont postulé
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name