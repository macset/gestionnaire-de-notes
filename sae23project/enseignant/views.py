from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EnseignantForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = EnseignantForm(request)
        if form.is_valid():
            enseignant = form.save()
            return render(request, 'enseignant/affiche.html', {'enseignant': enseignant, 'count': random()})
        else:
            return render(request, 'enseignant/ajout.html', {'form': form})
    else:
        form = EnseignantForm()
        return render(request, 'enseignant/ajout.html', {'form': form})


def traitement(request):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        enseignant = lform.save()
        return render(request, 'enseignant/affiche.html', {'enseignant': enseignant})
    else:
        return render(request, 'enseignant/ajout.html', {'form': lform})
    
    
def all(request):
    enseignants = list(models.Enseignant.objects.all())
    return render(request, 'enseignant/all.html', {'enseignants': enseignants})


def read(request,id):
    enseignant = models.Enseignant.objects.get(pk=id)
    return render(request, 'enseignant/affiche.html', {'enseignant': enseignant})

def traitementupdate(request, id):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        
        enseignant = lform.save(commit=False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("/enseignant/all/")
    else:
        return render(request, 'enseignant/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    enseignant = get_object_or_404(models.Enseignant, pk=id)
    form = EnseignantForm(instance=enseignant)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'enseignant/update.html', {'form': form, 'id': id})

def delete(request, id):
    enseignant = get_object_or_404(models.Enseignant, pk=id)
    enseignant.delete()
    return HttpResponseRedirect("/enseignant/all/")