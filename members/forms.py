from django import forms
from .models import Member

class JoinParlourForm(forms.ModelForm):
    class Meta:
        model = Member
        # On ne demande que ce que l'utilisateur doit remplir
        fields = ['full_name', 'email', 'bio', 'english_level']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full bg-[#1a1a1a] border border-gray-700 p-3 rounded text-white focus:border-[#D4AF37] outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full bg-[#1a1a1a] border border-gray-700 p-3 rounded text-white focus:border-[#D4AF37] outline-none'}),
            'bio': forms.Textarea(attrs={'class': 'w-full bg-[#1a1a1a] border border-gray-700 p-3 rounded text-white focus:border-[#D4AF37] outline-none', 'rows': 3}),
            'english_level': forms.Select(attrs={'class': 'w-full bg-[#1a1a1a] border border-gray-700 p-3 rounded text-white focus:border-[#D4AF37] outline-none'}),
        }