from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .HospitalDBConnect import *


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
    all_appointments = view_Appointments()
    context = {'appts': all_appointments}

    return HttpResponse(render(request, 'Hosptial/appointments.html', context))


def profile(request, patient_id):
    ''' shows patient profile '''

    # get the data for that id
    patient_profile = view_history(patient_id)
    context = {"profile": patient_profile[0]}

    return HttpResponse(render(request, 'Hosptial/profile.html', context))


def treatment(request, patient_id):
    ''' Handles treatment stuff '''

    # handle post, redirect to patient profile
    if request.method == 'POST':

        redirect('/hosptial/profile/' + patient_id)

    else:
        # get profile data for side display
        patient_profile = view_history(patient_id)

        # get all doctors
        all_doctors = view_Doctors()

        # set context
        context = {"profile": patient_profile[0], "doctors": all_doctors}

        return HttpResponse(
            render(request, 'Hosptial/create_treatment.html', context))


def update_appointment(request, patient_id, doc_id):
    ''' handles appointments update '''

    # handle get
    if request.method == 'GET':
        # get old apt data and pass it as context

        # get all doctors
        all_doctors = view_Doctors()
        context = {
            'doctors': all_doctors,
            'PatientID': patient_id,
            'DocID': doc_id
        }
        return HttpResponse(
            render(request, 'Hosptial/update_appt.html', context))

    else:
        prefered_doctor = request.POST.get("preferedDoctor", "")
        prefered_date = request.POST.get("preferedDate", "")
        reason = request.POST.get("reason", "")

        Update_Appointment(
            int(patient_id), int(doc_id.strip('/')), int(prefered_doctor),
            str(prefered_date), reason)
        return redirect('/hosptial/appointments/')


def patients(request):
    ''' shows all patients and leads to profile '''
    # get data
    all_patients = view_Patients()
    context = {'patients': all_patients}

    return HttpResponse(render(request, 'Hosptial/patients.html', context))


def doctors(request):
    ''' shows all doctors and their info '''

    # get all the data
    all_doctors = view_Doctors()
    context = {'doctors': all_doctors}
    return HttpResponse(render(request, 'Hosptial/doctors.html', context))


def rooms(request):
    ''' shows info about rooms: handles get only '''

    # get all data and set context
    all_rooms = view_Rooms()
    context = {'rooms': all_rooms}

    return HttpResponse(render(request, 'Hosptial/rooms.html', context))


def departments(request):
    ''' shows dep info: handles get only '''
    # get data
    all_departments = view_Departments()

    context = {'departments': all_departments}

    return HttpResponse(render(request, 'Hosptial/departments.html', context))


def bills(request):
    ''' just shows all the bills '''

    # get all the data
    all_bills = view_Bills()
    context = {'bills': all_bills}

    return HttpResponse(render(request, 'Hosptial/bills.html', context))


def create_bill(request, patient_id):
    ''' handles the view and creation of bills '''

    return HttpResponse(render(request, 'Hosptial/create_bill.html'))


def delete_bill(request, bill_num):
    ''' deletes a bill given the bill_id '''

    return redirect('/hosptial/bills')
