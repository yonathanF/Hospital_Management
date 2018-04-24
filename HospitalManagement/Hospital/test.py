#print(view_Rooms())
#print(view_Employees())
#print(view_Departments())
#print(view_Doctors())
#print(view_Bills())
#print(view_Appointments())
#print(view_Patients())
#print(view_history(104))
from datetime import date

from HospitalDBConnect import *

#InsertPatient(192, 'Hussain', 'Zakir', '4342285612',
# '190 Institute Hills Charlottesville VA')

#InsertAppt(172, 'Doc12', '2018-04-22', 'Severe Headache')

#print(view_Bill(103))

#print(Update_Appointment(101, 5, 5, '2018-05-31', 'test Reason'))
#DeleteBill(123)

#InsertBill(104, '2018-04-25', 3092, 'some description', '2018-04-27')
InsertTreatment('test sick', '2018-05-31', 'sick bars', 'might catch on fire')
