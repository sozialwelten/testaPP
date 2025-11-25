from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from typing import cast

from testapp.models.libraries import Library, CmtNotes
from testapp.models.profiles import UserProfile

def lib_index(request) -> HttpResponse:
    libs = get_object_or_404(Library.objects.all())

    return render(request, 'index.html', {
        'id': libs.id,
        'owner': libs.owner or ("INSTANCE PUBLIC"),
    })

def user_lib_idx(request, username: str) -> HttpResponse:
    libs = get_object_or_404(UserProfile, user__username=username).libraries
    return render(request, "index.html", {
        'id': libs.id,
        ''
    })



def lib_comments_index(request, ) -> HttpResponse:
    lib = get_object_or_404(Library, id=lib_id)
    comments: CmtNotes = get_object_or_404(lib.notes.all()) # type: ignore

    long, lat = (str(lib.long).replace(".", "_"), str(lib.lat).replace(".", "_"))
    return render(request, "index.html", {
        'id': comments.id,
        'author': comments.author,
        'comment': comments.short
    })
