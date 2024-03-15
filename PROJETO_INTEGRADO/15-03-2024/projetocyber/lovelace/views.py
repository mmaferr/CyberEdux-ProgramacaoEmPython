from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def homepage_view(request):
    return render(request, 'homepage.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'login_incorreto': False
        })
    elif request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {
                'login_incorreto': True
            })
        
def cadastrar_view(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    elif request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(username=email).exists():
            return HttpResponse("Já existe um cadastro com este email!")
        user = User.objects.create_user(email, email, senha)
        login(request, user)
        return redirect('/')
    else:
        return HttpResponseBadRequest()        

def sobre_view(request):
    return render(request, 'sobre.html')

def linguagens_view(request):
    return render(request, 'linguagens.html')

def cursos_view(request):
    return render(request, 'cursos.html')