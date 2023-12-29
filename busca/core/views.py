from django.shortcuts import render, redirect
from .models import Curso, Area, Publico
from .forms import CursoForm, AreaForm, UsuarioForm, PublicoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

decorator_with_arguments = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)
@decorator_with_arguments
def custom_permission_required(function, perm):
    def _function(request, *args, **kwargs):
        if request.user.has_perm(perm):
            return function(request, *args, **kwargs)
        else:
            #request.user.message_set.create(message = "Não tem permissão de acesso")
            messages.error(request, 'Usuário não tem permissão de acesso')
            #return render(request, 'registration/login.html')
            return redirect('home')
    return _function

#@login_required
#@permission_required('core.coordenador')
@custom_permission_required('core.coordenador')
def contato(request):
    return render(request, 'contato.html')

'''
    if request.user.is_active:
        if request.user.has_perm('core.coordenador'):
            return render(request, 'contato.html')
        else:
            erro = 'Não tem permissão de coordenador'
    else:
        erro = 'Usuário não autenticado'
    contexto = {
        'erro': erro
    }
    return render(request, 'registration/login.html', contexto)
'''
def dados_url(request, sobrenome, idade, nota):
    
    nota_final = float(nota)*10

    contexto = {
        'sobrenome':sobrenome,
        'idade':idade,
        'nota':nota_final
        }
    return render(request, 'dados_url.html', contexto)


# ============ CRUD CURSOS ==============

def cursos(request):
    titulo = ''
    vagas = ''
    areas=Area.objects.all()
    if request.POST:
        titulo = request.POST['titulo']
        area = request.POST['area']
        if area =="-1":
            if request.POST:
                vagas = int(request.POST['vagas'])            
                lista_cursos = Curso.objects.filter(titulo__contains = titulo).filter(vagas=vagas).filter(area_id=areas)
            else:
                lista_cursos = Curso.objects.filter(titulo__contains = titulo).filter(area_id=areas)
        else:
            if request.POST['vagas']:
                vagas = int(request.POST['vagas'])            
                lista_cursos = Curso.objects.filter(titulo__contains = titulo).filter(vagas=vagas).filter(area_id=areas)
            else:
                lista_cursos = Curso.objects.filter(titulo__contains = titulo).filter(vagas=vagas)
    else:
        lista_cursos = Curso.objects.all()

    contexto = {
        'lista_cursos': lista_cursos,
        'titulo':titulo,
        'vagas':vagas,
        'areas':areas
    }
    return render(request, 'cursos.html', contexto)


def curso_cadastro(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)

def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')


# ============ CRUD ÁREAS ==============

def areas(request):
    lista_areas = Area.objects.all()
    contexto = {
        'lista_areas': lista_areas
    }
    return render(request, 'areas.html', contexto)

def area_cadastro(request):
    
    form  = AreaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('areas')
    contexto = {
        'form': form
    }
    return render(request, 'area_cadastro.html', contexto)


# ============ CRUD PÚBLICOS ==============

def publicos(request):
    lista_publicos = Publico.objects.all()
    contexto = {
        'lista_publicos': lista_publicos
    }
    return render(request, 'publicos.html', contexto)

def publico_cadastro(request):
    form  = PublicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('publicos')
    contexto = {
        'form': form
    }
    return render(request, 'publico_cadastro.html', contexto)


@login_required
def perfil(request):
    return render(request, 'perfil.html')


def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            contexto = {
                'erro': 'Verifique usuário e/ou senha'
            }
            return render(request, 'registration\login.html', contexto)
    else:
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('home')

def cadastrar(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.save()
        
        # Recupera a opção marcada no formulário de perfil
        permissao_selecionada = request.POST['permissao']

        # Recuperar a permissão selecionada do BD
        permissao = Permission.objects.get(codename=permissao_selecionada)

        # Adicionar a permissão ao usuário que está sendo cadastrado
        usuario.user_permissions.add(permissao)

        usuario.save()
        return redirect('login')
    contexto = {
        'form': form
    }
    return render(request, 'registration\cadastro.html', contexto)
