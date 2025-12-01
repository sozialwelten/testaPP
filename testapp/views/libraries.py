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
