from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    ''' handles the registeration process '''

    return HttpResponse(render(request, 'Auth/register.html'))


def signin(request):
    ''' signs people in into our application '''

    return HttpResponse(render(request, 'Auth/register.html'))
