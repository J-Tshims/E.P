from django.shortcuts import render, redirect
from .models import Member
from .forms import JoinParlourForm

def member_list(request):
    # SI l'utilisateur a cliqué sur "Envoyer"
    if request.method == 'POST':
        form = JoinParlourForm(request.POST)
        if form.is_valid():
            form.save() # C'est ici que l'utilisateur est créé avec is_approved=False par défaut !
            return redirect('home')
    else:
        form = JoinParlourForm()

    approved_members = Member.objects.filter(is_approved=True)
    return render(request, 'members/member_list.html', {
        'members': approved_members,
        'form': form
    })