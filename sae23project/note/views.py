from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import NoteForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = NoteForm(request)
        if form.is_valid():
            note = form.save()
            return render(request, 'note/affiche.html', {'note': note, 'count': random()})
        else:
            return render(request, 'note/ajout.html', {'form': form})
    else:
        form = NoteForm()
        return render(request, 'note/ajout.html', {'form': form})


def traitement(request):
    lform = NoteForm(request.POST)
    if lform.is_valid():
        note = lform.save()
        return render(request, 'note/affiche.html', {'note': note})
    else:
        return render(request, 'note/ajout.html', {'form': lform})
    
    
def all(request):
    notes = list(models.Note.objects.all())
    return render(request, 'note/all.html', {'notes': notes})


def read(request,id):
    note = models.Note.objects.get(pk=id)
    return render(request, 'note/affiche.html', {'note': note})

def traitementupdate(request, id):
    lform = NoteForm(request.POST)
    if lform.is_valid():
        
        note = lform.save(commit=False)
        note.id = id
        note.save()
        return HttpResponseRedirect("/note/all/")
    else:
        return render(request, 'note/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    etudiant = get_object_or_404(models.Note, pk=id)
    form = NoteForm(instance=etudiant)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'appsae/update.html', {'form': form, 'id': id})

def delete(request, id):
    etudiant = get_object_or_404(models.Note, pk=id)
    etudiant.delete()
    return HttpResponseRedirect("/appsae/all/")