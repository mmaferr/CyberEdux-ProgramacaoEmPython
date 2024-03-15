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
]