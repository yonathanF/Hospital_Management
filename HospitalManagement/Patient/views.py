from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    ''' a patient private home page '''
    return HttpResponse(render(request, 'Patient/home.html'))


def appointments(request):
    ''' handles the creation and display of appts '''

    return HttpResponse(render(request, 'Patient/appt.html'))


def new_appointments(request):
    ''' handles the creation and display of appts '''

    if request.method == 'POST':
        # get the data
        doctor = request.POST.get("preferedDoctor", "")
        apt_date = request.POST.get("preferedDate", "")
        reason = request.POST.get("reason", "")

        #TODO insert into db
        return redirect("/patient/home/")

    else:
        return HttpResponse(render(request, 'Patient/new_appt.html'))


def medications(request):
    ''' mediations info page'''

    # no post, handle all as get
    return HttpResponse(render(request, 'Patient/medications.html'))


def bills(request):
    ''' shows the user profile '''

    # also no posts, all get
    return HttpResponse(render(request, 'Patient/bills.html'))
