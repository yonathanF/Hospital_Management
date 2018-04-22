from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    ''' a patient private home page '''
    context = {}
    context['username'] = request.user.first_name
    return HttpResponse(render(request, 'Patient/home.html', context))


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
        return redirect("/patient/appointments/")

    else:
        return HttpResponse(render(request, 'Patient/new_appt.html'))


def medications(request):
    ''' mediations info page'''

    # no post, handle all as get
    return HttpResponse(render(request, 'Patient/medications.html'))

def drug_more(request):
    ''' mediations info page'''

    # no post, handle all as get
    return HttpResponse(render(request, 'Patient/drug_more.html'))


def bills(request):
    ''' shows the user profile '''

    # also no posts, all get
    return HttpResponse(render(request, 'Patient/bills.html'))

def bills_more(request):
    ''' shows the user profile '''

    # also no posts, all get
    return HttpResponse(render(request, 'Patient/bills_more.html'))
