from django.contrib import admin
from django.urls import path
from lovelace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='home'),
    path('login', views.login_view, name='login'),
    path('cadastrar', views.cadastrar_view, name='cadastrar'),
    path('sobre', views.sobre_view, name='sobre'),
    path('linguagens', views.linguagens_view, name='linguagens'),
    path('cursos', views.linguagens_view, name='cursos'),
    path('cursos-aluno', views.cursos_aluno_view, name='cursos-aluno'),   
    path('portal-do-aluno', views.portal_do_aluno_view, name='portal-do-aluno'),   
    path('meus-cursos/<int:id>', views.meus_cursos_view, name='meus-cursos'), 
    path('portal-do-aluno-curso', views.portal_do_aluno_curso_view, name='portal-do-aluno'), 
    path('nossos-cursos', views.nossos_cursos_view, name='nossos-cursos'), 
]