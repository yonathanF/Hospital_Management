from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    ''' the home for hosptial admins '''

    # handle get only
    return HttpResponse(render(request, 'Hosptial/home.html'))


def search(request):
    ''' search for firstname, lastname, email '''

    return HttpResponse(render(request, 'Hosptial/search.html'))
