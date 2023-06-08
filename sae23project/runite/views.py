from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RuniteForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = RuniteForm(request)
        if form.is_valid():
            runite = form.save()
            return render(request, 'runite/affiche.html', {'runite': runite, 'count': random()})
        else:
            return render(request, 'runite/ajout.html', {'form': form})
    else:
        form = RuniteForm()
        return render(request, 'runite/ajout.html', {'form': form})


def traitement(request):
    lform = RuniteForm(request.POST)
    if lform.is_valid():
        runite = lform.save()
        return render(request, 'runite/affiche.html', {'runite': runite})
    else:
        return render(request, 'runite/ajout.html', {'form': lform})
    
    
def all(request):
    runites = list(models.Runite.objects.all())
    return render(request, 'runite/all.html', {'runites': runites})


def read(request,id):
    runite = models.Runite.objects.get(pk=id)
    return render(request, 'runite/affiche.html', {'runite': runite})

def traitementudpate(request, id):
    lform = RuniteForm(request.POST)
    if lform.is_valid():
        
        runite = lform.save(commit=False)
        runite.id = id
        runite.save()
        return HttpResponseRedirect("/runite/all/")
    else:
        return render(request, 'runite/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    runite = get_object_or_404(models.Runite, pk=id)
    form = RuniteForm(instance=runite)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'runite/update.html', {'form': form, 'id': id})

def delete(request, id):
    runite = get_object_or_404(models.Runite, pk=id)
    runite.delete()
    return HttpResponseRedirect("/runite/all/")

# Create your views here.
