from django.shortcuts import render
#o render gera o protoclo http com uma página html

#criando a sua view
def home(request):
    return render(request, 'index.html')