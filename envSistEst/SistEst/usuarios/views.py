from urllib import request
from django.shortcuts import render, redirect
from .forms import AcessForm, RegisterForms
from django.http import Http404
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login

# Create your views here.
def register_view(request, firstacess=0):

    if firstacess == 1:
        register_form = request.session.get("register_form", None)
        form = RegisterForms(register_form)
    else:
        if request.session.get("register_form"):
            del(request.session["register_form"])
        form = RegisterForms()

    register_form = request.session.get("register_form",None )

    form = RegisterForms(register_form)

    form = RegisterForms()
    return render(request, 'pages/register_view.html', {'form': form})

def register_create(request):
    if not request.POST:
        raise Http404()

    post = request.POST
    request.session["register_form"] = post

    form = RegisterForms(post)

    if form.is_valid():
        form.save()
        user = form.save(commit=False)
        user.set_password(make_password(user.password))
        user.save()
        messages.success(request, "Usuario cadastrado com sucesso")
        del(request.session["register_form"])

    return redirect('usuarios:register', firstacess=1)


def login_view(request):
    if request.POST:
        form_data = request.POST
        form = AcessForm(form_data)
    else:
        form = AcessForm()

    return render(request, 'pages/login_view.html',{'form':form} )

def login_acess(request):

    if not request.POST:
        raise Http404()
    
    post = request.POST

    form = AcessForm(post)

    if form.is_valid():
        usern = post['username']
        passwd = post['password']

        user = User.objects.filter(username = usern)

        if user:
            check_p = check_password(passwd, user[0].password)
            authenticad_user = authenticate(username =usern, password= passwd)
            if check_p:
                messages.success(request, 'Usuario Logado com Sucesso.')
                login(request, authenticad_user)
                return redirect('usuario:area_usuario')
            else:
                messages.error(request, 'Login e senha não conferem.')
        else:
            messages.error(request, 'Login e senha não conferem.')
    else:
        messages.error(request,'Dados do formulario invalidos' )
   
    return redirect('usuarios:login')


def area_usuario_view(request):

    return render(request, 'pages/area_usuario_view.html')
