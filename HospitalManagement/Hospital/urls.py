from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/home', views.home, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^/search', views.search, name='search'),
    url(r'^/treatment/(?P<patient_id>[0-9]+)/',
        views.treatment,
        name='treatment'),
    url(r'^/appointments', views.appointments, name='appointments'),
    url(r'^/patients', views.patients, name='patients'),
    url(r'^/doctors', views.doctors, name='doctors'),
    url(r'^/nurses', views.nurses, name='nurses'),
    url(r'^/employees', views.employees, name='employees'),
    url(r'^/rooms', views.rooms, name='rooms'),
    url(r'^/bills_more/(?P<billNumber>[0-9]+)/$', views.bills_more, name='bills_more'),
    url(r'^/bills', views.bills, name='bills'),
    url(r'^/departments', views.departments, name='departments'),
    url(r'^/create_bill/(?P<patient_id>[0-9]+)/$',
        views.create_bill,
        name='create_bill'),
    url(r'^/delete_bill/(?P<bill_num>[0-9]+)/$',
        views.delete_bill,
        name='delete_bill'),
    url(r'^/profile/(?P<patient_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^/update_appointment/(?P<patient_id>[0-9]+)/(?P<doc_id>[0-9]+/)$',
        views.update_appointment,
        name='update_appointment')
]
