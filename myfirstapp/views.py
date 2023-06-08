from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myfirstapp/index.html')


def form(request):
    return render(request, 'myfirstapp/form.html')

def bonjour(request):
    nom=request.GET['nom']
    return render(request, 'myfirstapp/bonjour.html', {'nom': nom})

def main(request):
    return render(request, 'myfirstapp/main.html')

def enseignement(request):
    if request.method == 'POST':
        # 处理表单提交
        if 'save_student' in request.POST:
            # 处理保存学生信息的逻辑
            student_id = request.POST.get('student_id')
            student_nom = request.POST.get('student_nom')
            student_prenom = request.POST.get('student_prénom')
            student_group = request.POST.get('student_group')
            student_photo = request.POST.get('student_photo')
            student_email = request.POST.get('student_email')
            # 执行保存学生信息的操作

        elif 'save_ue' in request.POST:
            # 处理保存UE信息的逻辑
            ue_code = request.POST.get('ue_code')
            ue_nom = request.POST.get('ue_nom')
            ue_semestre = request.POST.get('ue_semestre')
            ue_credit_ects = request.POST.get('ue_créditECTS')
            # 执行保存UE信息的操作

        elif 'save_resource' in request.POST:
            # 处理保存资源信息的逻辑
            resource_code = request.POST.get('resource_code')
            resource_nom = request.POST.get('resource_nom')
            resource_descriptif = request.POST.get('resource_descriptif')
            resource_coefficient = request.POST.get('resource_coefficient')
            # 执行保存资源信息的操作

        elif 'save_teacher' in request.POST:
            # 处理保存教师信息的逻辑
            enseignant_id = request.POST.get('enseignant_id')
            enseignant_nom = request.POST.get('enseignant_nom')
            enseignant_prenom = request.POST.get('enseignant_prénom')
            # 执行保存教师信息的操作

        # 处理完表单提交后的重定向或其他逻辑

    return render(request, 'myfirstapp/enseignement.html')
