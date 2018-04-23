from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/home', views.home, name='home'),
    url(r'^/appointments', views.appointments, name='appointments'),
    url(r'^/new_appointments', views.new_appointments,
        name='new_appointments'),
    url(r'^/medications', views.medications, name='medications'),
    url(r'^/drug_more/(?P<treatmentNumber>[0-9]+)/$', views.drug_more, name='drug_more'),
    url(r'^/bills_more/(?P<billNumber>[0-9]+)/$', views.bills_more, name='bills_more'),
    url(r'^/bills', views.bills, name='bills')
]
