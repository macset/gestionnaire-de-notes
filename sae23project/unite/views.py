from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UniteForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = UniteForm(request)
        if form.is_valid():
            unite = form.save()
            return render(request, 'bibliotheque/affiche.html', {'unite': unite, 'count': random()})
        else:
            return render(request, 'bibliotheque/ajout.html', {'form': form})
    else:
        form = UniteForm()
        return render(request, 'bibliotheque/ajout.html', {'form': form})


def traitement(request):
    lform = UniteForm(request.POST)
    if lform.is_valid():
        unite = lform.save()
        return render(request, 'unite/affiche.html', {'unite': unite})
    else:
        return render(request, 'unite/ajout.html', {'form': lform})
    
    
def all(request):
    unites = list(models.Unite.objects.all())
    return render(request, 'unite/all.html', {'unites': unites})


def read(request,id):
    unite = models.Unite.objects.get(pk=id)
    return render(request, 'unite/affiche.html', {'unite': unite})

def traitementupdate(request, id):
    lform = UniteForm(request.POST)
    if lform.is_valid():
        
        unite = lform.save(commit=False)
        unite.id = id
        unite.save()
        return HttpResponseRedirect("/unite/all/")
    else:
        return render(request, 'unite/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    unite = get_object_or_404(models.Unite, pk=id)
    form = UniteForm(instance=unite)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'unite/update.html', {'form': form, 'id': id})

def delete(request, id):
    unite = get_object_or_404(models.Unite, pk=id)
    unite.delete()
    return HttpResponseRedirect("/unite/all/")

# Create your views here.
