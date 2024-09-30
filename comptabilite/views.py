from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.forms import formset_factory

from . import forms
from . import models

@login_required
def compte_list(request):
    comptes = models.Compte.objects.all()
    return render(request, 'comptabilite/compte_list.html', context={'comptes': comptes})

@login_required
def create_compte(request):
    form = forms.CompteForm()
    if request.method == 'POST':
        form = forms.CompteForm(request.POST)
        if form.is_valid():
            compte = form.save(commit=False)
            compte.author = request.user 
            compte.save()
            return redirect('home')
    return render(request, 'comptabilite/create_compte.html', context={'form': form})

@login_required
def view_compte(request, compte_id):
    compte = get_object_or_404(models.Compte, id=compte_id)
    return render(request, 'comptabilite/view_compte.html', context={'compte': compte})

@login_required
def edit_compte(request, compte_id):
    compte = get_object_or_404(models.Compte, id=compte_id)
    form = forms.CompteForm(instance=compte)
    if request.method == "POST":
        form = forms.CompteForm(request.POST, instance=compte)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'comptabilite/edit_compte.html', context={'form':form})

@login_required
def ecriture_list(request):
    return render(request, 'comptabilite/ecriture_list.html')

@login_required
def create_ecriture(request):
    ecriture_form = forms.EcritureForm()
    MouvementFormsSet = formset_factory(forms.MouvementForm, extra=10)
    mouvement_formset = MouvementFormsSet()
    return render(request, 'comptabilite/create_ecriture.html', context={'ecriture_form': ecriture_form, 'mouvement_formset': mouvement_formset})

@login_required
def view_ecriture(request, ecriture_id):
    pass