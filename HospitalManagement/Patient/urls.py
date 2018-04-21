from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/home', views.home, name='home'),
    url(r'^/appointments', views.appointments, name='appointments'),
    url(r'^/new_appointments', views.new_appointments,
        name='new_appointments'),
    url(r'^/medications', views.medications, name='medications'),
    url(r'^/bills', views.bills, name='bills')
]
