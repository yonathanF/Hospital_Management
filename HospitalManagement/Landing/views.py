from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    ''' renders the landing html page ... everything is in the html for this '''

    return HttpResponse(render(request, 'Landing/index.html'))
