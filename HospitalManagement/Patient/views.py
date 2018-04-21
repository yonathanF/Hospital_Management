from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    ''' a patient private home page '''
    return HttpResponse(render(request, 'Patient/home.html'))
