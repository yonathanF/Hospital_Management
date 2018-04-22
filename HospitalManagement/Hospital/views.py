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


def appointments(request):
    ''' handles appointments '''

    return HttpResponse(render(request, 'Hosptial/appointments.html'))


def update_appointment(request, patient_id, doc_id):
    ''' handles appointments update '''

    return HttpResponse(render(request, 'Hosptial/update_appt.html'))


def patients(request):
    ''' shows all patients and leads to profile '''

    return HttpResponse(render(request, 'Hosptial/patients.html'))


def doctors(request):
    ''' shows all doctors and their info '''

    return HttpResponse(render(request, 'Hosptial/doctors.html'))


def rooms(request):
    ''' shows info about rooms: handles get only '''

    return HttpResponse(render(request, 'Hosptial/rooms.html'))


def departments(request):
    ''' shows dep info: handles get only '''

    return HttpResponse(render(request, 'Hosptial/departments.html'))


def bills(request):
    ''' handles the view and creation of bills '''

    return HttpResponse(render(request, 'Hosptial/bills.html'))


def delete_bill(request, bill_num):
    ''' deletes a bill given the bill_id '''

    return redirect('/hosptial/bills')
