from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest


def index_view(request):
    return HttpResponseRedirect('/feed')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'incorrect_login': False
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/feed')
        else:
            return render(request, 'login.html', {
            'incorrect_login': True
        })
    else:
        return HttpResponseBadRequest()

@login_required(login_url='/login')
def feed_view(request):
    username = request.user.username
    return render(request, 'feed.html', {
        'username': username
    })
