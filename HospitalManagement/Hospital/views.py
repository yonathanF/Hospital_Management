from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .HospitalDBConnect import *


def home(request):
    ''' the home for hosptial admins '''

    appt_count = view_appt_count()
    doc_count = view_doc_count()
    room_count = view_room_count()

    appt_count = appt_count[0]['count(PatientID)']
    doc_count = doc_count[0]['count(DocID)']
    room_count = room_count[0]['count(RoomNumber)']

    context = {
        "appt_count": appt_count,
        'doc_count': doc_count,
        'room_count': room_count
    }
    # handle get only
    return HttpResponse(render(request, 'Hosptial/home.html', context))


def search(request):
    ''' search for firstname, lastname, email '''

    # handle post
    if request.method == 'POST':

        # get data
        first_name = request.POST.get("firstName", "")
        last_name = request.POST.get("lastName", "")

        matching_patients = view_person_search_count(first_name, last_name)
        context = {'patients': matching_patients}

        # reorganize data and pass as context
        return HttpResponse(render(request, 'Hosptial/search.html', context))

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
    context = {"profile": patient_profile}

    return HttpResponse(render(request, 'Hosptial/profile.html', context))


def treatment(request, patient_id):
    ''' Handles treatment stuff '''

    # handle post, redirect to patient profile
    if request.method == 'POST':

        doc_id = request.POST.get("doctorName", "")
        aliment = request.POST.get("aliment", "")
        pre_date = request.POST.get("pdate", "")
        expected = request.POST.get("expected", "")
        warnings = request.POST.get("warnings", "")

        InsertTreatment(aliment, str(pre_date), str(expected), str(warnings))
        return redirect('/hosptial/profile/' + patient_id)

    else:
        # get profile data for side display
        patient_profile = view_history(patient_id)

        # get all doctors
        all_doctors = view_Doctors()

        # set context
        context = {"profile": patient_profile[-1], "doctors": all_doctors}

        return HttpResponse(
            render(request, 'Hosptial/create_treatment.html', context))


def update_appointment(request, patient_id, doc_id):
    ''' handles appointments update '''

    # handle get
    if request.method == 'POST':
        prefered_doctor = request.POST.get("preferedDoctor", "")
        prefered_date = request.POST.get("preferedDate", "")
        reason = request.POST.get("reason", "")

        Update_Appointment(
            int(patient_id), int(doc_id.strip('/')), int(prefered_doctor),
            str(prefered_date), reason)
        return redirect('/hosptial/appointments/')

    else:

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


def nurses(request):
    ''' shows all doctors and their info '''

    # get all the data
    all_nurses = view_Nurses()
    context = {'nurses': all_nurses}
    return HttpResponse(render(request, 'Hosptial/nurses.html', context))

def employees(request):
    ''' shows all doctors and their info '''

    # get all the data
    all_employees = view_Employees()
    context = {'employees': all_employees}
    return HttpResponse(render(request, 'Hosptial/employees.html', context))


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

    if request.method == 'POST':
        due_date = request.POST.get("dueDate", "")
        re_date = request.POST.get("reDate", "")
        amount = request.POST.get("amount", "")
        description = request.POST.get("description", "")

        InsertBill(
            int(patient_id), str(re_date), int(amount), str(description),
            str(due_date))

        return redirect('/hosptial/bills')

    context = {'PatientID': patient_id}
    return HttpResponse(render(request, 'Hosptial/create_bill.html', context))


def delete_bill(request, bill_num):
    ''' deletes a bill given the bill_id '''

    # call the delete function
    DeleteBill(bill_num)

    return redirect('/hosptial/bills')
