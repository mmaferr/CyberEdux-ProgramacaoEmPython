from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Aluno, Aula
from datetime import datetime

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
        if user is not None and not Aluno.objects.filter(user=user).exists():
            login(request, user)
            return redirect('/portal-do-aluno')
        else:
            return render(request, 'login.html', {
                'login_incorreto': True
            })
        
def cadastrar_view(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    elif request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        data_nascimento = request.POST['data_nascimento']  # Recupera a data de nascimento do formulário
        if User.objects.filter(username=email).exists():
            return HttpResponse("Já existe um cadastro com este email!")
        user = User.objects.create_user(email, email, senha, first_name=name)
        aluno = Aluno.objects.create(user=user, data_nascimento=datetime.strptime(data_nascimento, '%Y-%m-%d'))
        login(request, user)
        return redirect('/cursos-aluno')
    else:
        return HttpResponseBadRequest()        

def sobre_view(request):
    return render(request, 'sobre.html')

def linguagens_view(request):
    return render(request, 'linguagens.html')

def cursos_view(request):
    return render(request, 'cursos.html')

def cursos_aluno_view(request):
    return render(request, 'cursos-aluno.html')

def portal_do_aluno_view(request):
    return render(request, 'portal-do-aluno.html')

def portal_do_aluno_curso_view(request):
    return render(request, 'portal-do-aluno-curso.html')

def meus_cursos_view(request, id):
    cursos = {
        1: {'titulo': 'Desenvolvedor Full-stack', 'descricao': 'Domine programação front-end e back-end em um curso completo. Aprenda HTML, CSS, JavaScript, Python, Django e mais para criar aplicativos web profissionais.'},
        2: {'titulo': 'Desenvolvedor Front-end', 'descricao': 'Aprenda as habilidades essenciais para se tornar um desenvolvedor front-end. Explore HTML, CSS e JavaScript para criar interfaces web interativas e responsivas.'},
        3: {'titulo': 'Python', 'descricao': 'Aprenda Python para desenvolvimento web, análise de dados e automação. Python é uma linguagem de programação versátil e poderosa, amplamente utilizada em diversas áreas da computação.'},
        4: {'titulo': 'SQL', 'descricao': 'Domine SQL para manipular bancos de dados de forma eficiente. SQL é a linguagem padrão para gerenciamento de bancos de dados relacionais, permitindo realizar consultas, atualizações e modificações nos dados.'},
        5: {'titulo': 'HTML', 'descricao': 'Aprenda HTML para criar páginas web. HTML é a linguagem de marcação fundamental para a construção de páginas na internet, permitindo estruturar o conteúdo e definir sua aparência.'},
        6: {'titulo': 'Javascript', 'descricao': 'Explore JavaScript para tornar suas páginas web interativas. JavaScript é uma linguagem de programação de alto nível, amplamente utilizada para adicionar comportamento dinâmico às páginas web, como validação de formulários, animações e interações do usuário.'}
    }
    
    curso = cursos[id]
    return render(request, "portal-do-aluno-meus-cursos.html", {"titulo": curso["titulo"]}, {"descricao": curso["descricao"]})
    
  
    

def nossos_cursos_view(request, id):
    return render(request, 'portal-do-aluno-nossos-cursos.html')