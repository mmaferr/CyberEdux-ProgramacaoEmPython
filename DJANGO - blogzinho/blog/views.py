from django.shortcuts import render

def feed(request):
    context = {
        'posts': [
            {'autor': 'Fulano, 'date': '01/02/2024', 'content': 'kjewblfewbflkbflkwflwfkew'},
            {'autor': 'Ciclano, 'date': '02/02/2024', 'content': 'kjewblfewbflkbflkwflwfkew'},
            {'autor': 'Beltrano, 'date': '03/02/2024', 'content': 'kjewblfewbflkbflkwflwfkew'}
        ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method == 'POST':
        author = request.POST.get("author")
        content = request.POST.get("content")
        print(author)
        print(content)
    return render(request, 'publicate.html')
