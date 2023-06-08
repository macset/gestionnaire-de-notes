from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ExamensForm
from . import models
from django.shortcuts import get_object_or_404

def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = ExamensForm(request)
        if form.is_valid():
            examens = form.save()
            return render(request, 'examens/affiche.html', {'examens': examens, 'count': random()})
        else:
            return render(request, 'examens/ajout.html', {'form': form})
    else:
        form = ExamensForm()
        return render(request, 'examens/ajout.html', {'form': form})


def traitement(request):
    lform = ExamensForm(request.POST)
    if lform.is_valid():
        examens = lform.save()
        return render(request, 'examens/affiche.html', {'examens': examens})
    else:
        return render(request, 'examens/ajout.html', {'form': lform})
    
    
def all(request):
    examenss = list(models.Examens.objects.all())
    return render(request, 'examens/all.html', {'examenss': examenss})


def read(request,id):
    examens = models.Examens.objects.get(pk=id)
    return render(request, 'examens/affiche.html', {'examens': examens})

def traitementupdate(request, id):
    lform = ExamensForm(request.POST)
    if lform.is_valid():
        
        examens = lform.save(commit=False)
        examens.id = id
        examens.save()
        return HttpResponseRedirect("/examens/all/")
    else:
        return render(request, 'examens/update.html', {'form': lform, 'id': id})
        
    return HttpResponse("ok") 


def update(request, id):
    examens = get_object_or_404(models.Examens, pk=id)
    form = ExamensForm(instance=examens)
    """
    if request.method == 'POST':
        form = LivreForm(instance=livre)
        if form.is_valid():
            form.save()
            return redirect('nom-de-la-page')
    """
    return render(request, 'examens/update.html', {'form': form, 'id': id})

def delete(request, id):
    examens = get_object_or_404(models.Examens, pk=id)
    examens.delete()
    return HttpResponseRedirect("/examens/all/")