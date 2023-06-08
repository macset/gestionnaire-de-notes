from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ExamensForm , LoginForm
from . import models
from django.shortcuts import get_object_or_404



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'toto' and password == 'toto':
            # 用户名和密码验证通过，执行跳转逻辑
            return redirect('/gestionnote/ajout/')
        
        if username == 'prof' and password == 'prof':
            # 用户名和密码验证通过，执行跳转逻辑
            return redirect('/gestionnote/ajout/')
        
        # 验证失败，显示错误信息
        error_message = "Invalid username or password."
        return render(request, 'gestionnote/login.html', {'error_message': error_message})
    
    return render(request, 'gestionnote/login.html')


def main(request):
    return render(request, 'gestionnote/main.html')



def login(request):
    return render(request, 'gestionnote/login.html')



def random() -> int:
    return 4 
def ajout(request):
    if request.method == "POST":
        
        form = ExamensForm(request)
        if form.is_valid():
            examens = form.save()
            return render(request, 'gestionnote/affiche.html', {'examens': examens, 'count': random()})
        else:
            return render(request, 'gestionnote/ajout.html', {'form': form})
    else:
        form = ExamensForm()
        return render(request, 'gestionnote/ajout.html', {'form': form})


def traitement(request):
    lform = ExamensForm(request.POST)
    if lform.is_valid():
        examens = lform.save()
        return render(request, 'gestionnote/affiche.html', {'examens': examens})
    else:
        return render(request, 'gestionnote/ajout.html', {'form': lform})
    
    
def all(request):
    examenss = list(models.Examens.objects.all())
    return render(request, 'gestionnote/all.html', {'examenss': examenss})


def read(request,id):
    examens = models.Examens.objects.get(pk=id)
    return render(request, 'gestionnote/affiche.html', {'examens': examens})

def traitementupdate(request, id):
    lform = ExamensForm(request.POST)
    if lform.is_valid():
        
        examens = lform.save(commit=False)
        examens.id = id
        examens.save()
        return HttpResponseRedirect("/gestionnote/all/")
    else:
        return render(request, 'gestionnote/update.html', {'form': lform, 'id': id})
        
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
    return render(request, 'gestionnote/update.html', {'form': form, 'id': id})

def delete(request, id):
    examens = get_object_or_404(models.Examens, pk=id)
    examens.delete()
    return HttpResponseRedirect("/gestionnote/all/")





