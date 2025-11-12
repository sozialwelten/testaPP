from django.shortcuts import render, get_object_or_404
from testapp.models import bookcaches

def cache_index(request):
    caches = bookcaches.BookCaches.objects.all
    return render(request, 'caches/index.html')

def comments_index(request,
                   cache = bookcaches.BookCaches):
    comments: bookcaches.Comments = cache.comments.all()                 # pyright: ignore
    long, lat = (str(cache.long).replace(".", "_"),
                 str(cache.lat).replace(".", "_"))
    return render(request,
                  f'cache/{long}/{lat}/comments',
                  {'id': comments.id,
                   'author': comments.author,
                   'comment': comments.short
                   })
    

