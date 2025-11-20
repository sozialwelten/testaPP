from django.shortcuts import render, get_object_or_404
from django.http import Http404
from testapp.models.bookcaches import BookCaches, CmtNotes

def cache_index(request):
    caches = get_object_or_404(BookCaches.objects.all())
    if isinstance(caches, Http404):
        return caches
    return render(request, 'caches/index.html', {
        'id': caches.id,
        'owner': caches.owner
    })

def cache_bcnotes_idx(request, cache = BookCaches):
    notes: CmtNotes|Http404 = get_object_or_404(cache.notes.all())

    if isinstance(notes, Http404):
        return notes

    long, lat = (str(cache.long).replace(".", "_"), str(cache.lat).replace(".", "_"))
    return render(request, f'cache/{long}/{lat}/comments', {
        'id': notes.id,
        'author': notes.author,
        'comment': notes.short
    })
