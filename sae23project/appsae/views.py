from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EtudiantForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = EtudiantForm(request)
        if form.is_valid():
            etudiant = form.save()
            return render(request, 'appsae/affiche.html', {'etudiant': etudiant, 'count': random()})
        else:
            return render(request, 'appsae/ajout.html', {'form': form})
    else:
        form = EtudiantForm()
        return render(request, 'appsae/ajout.html', {'form': form})


def traitement(request):
    lform = EtudiantForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save()
        return render(request, 'appsae/affiche.html', {'etudiant': etudiant})
    else:
        return render(request, 'appsae/ajout.html', {'form': lform})
    
    
def all(request):
    etudiants = list(models.Etudiant.objects.all())
    return render(request, 'appsae/all.html', {'etudiants': etudiants})


def read(request,id):
    etudiant = models.Etudiant.objects.get(pk=id)
    return render(request, 'appsae/affiche.html', {'etudiant': etudiant})

def traitementupdate(request, id):
    lform = EtudiantForm(request.POST)
    if lform.is_valid():
        
        etudiant = lform.save(commit=False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("/appsae/all/")
    else:
        return render(request, 'appsae/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)
    form = EtudiantForm(instance=etudiant)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'appsae/update.html', {'form': form, 'id': id})

def delete(request, id):
    etudiant = get_object_or_404(models.Etudiant, pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/appsae/all/")
