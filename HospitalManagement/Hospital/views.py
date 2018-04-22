from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    ''' the home for hosptial admins '''

    # handle get only
    return HttpResponse(render(request, 'Hosptial/home.html'))


def search(request):
    ''' search for firstname, lastname, email '''

    # handle post
    if request.method == 'POST':

        # get data

        first_name = request.POST.get("firstName", "")
        last_name = request.POST.get("lastName", "")
        email = request.POST.get("email", "")

        if first_name and last_name and email:
            pass  # call function with all args
        elif first_name and last_name:
            pass  # call function with two args
        elif email:
            pass  # call with email only
        elif first_name:
            pass  # call w/ fname only
        elif last_name:
            pass  # call w/ lname only

        # reorganize data and pass as context
        return HttpResponse(render(request, 'Hosptial/search.html'))

    else:
        return HttpResponse(render(request, 'Hosptial/search.html'))


def appointments(request):
    ''' handles appointments '''

    # get all appointments
    return HttpResponse(render(request, 'Hosptial/appointments.html'))


def profile(request, patient_id):
    ''' shows patient profile '''

    return HttpResponse(render(request, 'Hosptial/profile.html'))


def treatment(request, patient_id):
    ''' Handles treatment stuff '''

    # handle post, redirect to patient profile
    if request.method == 'POST':

        redirect('/hosptial/profile/' + patient_id)

    else:
        return HttpResponse(render(request, 'Hosptial/create_treatment.html'))


def update_appointment(request, patient_id, doc_id):
    ''' handles appointments update '''

    # handle get
    if request.method == 'GET':
        # get old apt data and pass it as context
        return HttpResponse(render(request, 'Hosptial/update_appt.html'))

    else:
        prefered_doctor = request.POST.get("firstName", "")
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
