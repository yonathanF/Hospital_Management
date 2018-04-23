from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .HospitalDBConnect import *

def home(request):
    ''' a patient private home page '''
    context = {}
    context['username'] = request.user.first_name
    return HttpResponse(render(request, 'Patient/home.html', context))


def appointments(request):
    ''' handles the creation and display of appts '''
    all_appointments = view_Appointments()
    context = {'appts': all_appointments}

    return HttpResponse(render(request, 'Patient/appt.html', context))


def new_appointments(request):
    ''' handles the creation and display of appts '''

    if request.method == 'POST':
        # get the data
        PatientID = request.user.id
        DocID = request.POST.get("preferedDoctor", "")
        Date = request.POST.get("preferedDate", "")
        Reason = request.POST.get("reason", "")
        InsertAppt(PatientID, DocID, Date, Reason)
        #TODO insert into db
        return redirect("/patient/appointments/")

    else:
        return HttpResponse(render(request, 'Patient/new_appt.html'))


def medications(request):
    ''' mediations info page'''
    PatientID = request.user.id
    all_treatments = view_Treatment(PatientID)
    context = {'treatments': all_treatments}

    # no post, handle all as get
    return HttpResponse(render(request, 'Patient/medications.html'))

def drug_more(request):
    ''' mediations info page'''

    # no post, handle all as get
    return HttpResponse(render(request, 'Patient/drug_more.html'))


def bills(request):
    ''' shows the user profile '''

    # also no posts, all get
    all_bills = view_Bills()
    context = {'bills': all_bills}
    return HttpResponse(render(request, 'Patient/bills.html', context))

def bills_more(request):
    ''' shows the user profile '''

    # also no posts, all get
    return HttpResponse(render(request, 'Patient/bills_more.html'))
