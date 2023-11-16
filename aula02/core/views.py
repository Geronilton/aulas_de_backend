from django.shortcuts import render, redirect
from .models import curso, Area
from .forms import CursosForm, AreasForm, UsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def dados_url(request, sobrenome, idade,nota):

    nota_final = float(nota)*10
    contexto = {
        'sobrenome':sobrenome,
        'idade':idade,
        'nota':nota_final
    }
    return render(request, 'dados_url.html',contexto)

#*********** CRUD Cursos *********************

def cursos(request):
    lista_cursos = curso.objects.all()
    contexto = {
        'lista_cursos': lista_cursos,
    }

    return render(request, 'cursos.html',contexto)

def curso_cadastro(request):
    form = CursosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    contexto = {
        'form' : form,
    }

    return render(request, 'curso_cadastro.html', contexto)


def curso_editar(request, id):
    Curso = curso.objects.get(pk=id)
    form = CursosForm(request.POST or None, instance = Curso)

    if form.is_valid():
        form.save()
        return redirect('cursos')

    contexto = {
        'form' : form,
    }

    return render(request, 'curso_cadastro.html',contexto)

def curso_remover(request,id):
    Curso = curso.objects.get(pk=id)
    Curso.delete()

    return redirect('cursos')

# ************** CRUD AREA **********

def area(request):
    lista_Area = Area.objects.all()

    contexto = {
        'lista_Area': lista_Area,
    }
    return render(request, 'area.html', contexto)

def cadastrar_area(request):
    form =  AreasForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('area')

    contexto = {
        'form' : form,
    }

    return render(request, 'cadastrar_area.html', contexto)

def editar_area(request, id):
    area= Area.objects.get(pk=id)
    form = AreasForm(request.POST or None,instance=area)

    if form.is_valid():
        form.save()
        return redirect('area')

    contexto = {
        'form' : form,
    }

    return render(request, 'cadastrar_area.html', contexto)

def deletar_area(request, id):
    area = Area.objects.get(pk= id)
    area.delete()

    return redirect('area')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario,password= senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')


def desconectar(request):
    logout(request)
    return redirect('home')


def cadastrar(request):
    form = UsuarioForm(request.POST or None )
    if form.is_valid():
        form.save()
        return redirect('login')
    
    contexto ={
        'form':form
    }
    return render(request, 'registration/cadastro.html',contexto)