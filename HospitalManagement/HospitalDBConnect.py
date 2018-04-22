# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:42:10 2018

@author: Thinkpad
"""

##########################################################################################################################


'This block inserts Patient record into database'
def InsertPatient(PatientID, First_Name, Last_Name, PhoneNumber, Address):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_Insert = "INSERT INTO Patient (PatientID, FirstName, LastName, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
    PatientDetails = (PatientID, First_Name, Last_Name, PhoneNumber, Address)
    cursor.execute(sql_Insert, PatientDetails)
    conn.commit()
    conn.close()
#Test function
#InsertPatient(192,'Hussain', 'Zakir', '4342285612', '190 Institute Hills Charlottesville VA')
##########################################################################################################################


'This block inserts Docctors record into the database'
def InsertDoctor(DocID, FirstName, LastName, Address, Phone, Email, Salary):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect")
        
    sql_Insert = "INSERT INTO Doctor (DocID, FirstName, LastName, Address, Phone, Email, Salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    DoctorDetails = (DocID, FirstName, LastName, Address, Phone, Email, Salary)
    cursor.execute(sql_Insert, DoctorDetails)
    conn.commit()
    conn.close()
#Test function
#InsertDoctor('Doc12','Yohanthan', 'Fiseha', '520 Lambert Hills Charlottesville VA', '4342229812', 'y2kf@virginia.edu', '150000')
###########################################################################################################################


'This block creates appointment between patient and doctor'        
def InsertAppt(PatientID, DocID, Date, Reason):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_InsertAppt = "INSERT INTO Appointment (PatientID, DocID, ApptDate, Reason) VALUES (%s, %s, %s, %s)"
    ApptDetails = (PatientID, DocID, Date, Reason)
    cursor.execute(sql_InsertAppt, ApptDetails)
    conn.commit()
    conn.close()
#Test function
#InsertAppt(172, 'Doc12', '2018-04-22', 'Severe Headache')    
###########################################################################################################################
   
"This block creates view of Patient's appointments with doctors"
def view_Appointment(PatientID):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Appointment AS SELECT PatientID, FirstName, ApptDate, Reason 
    FROM Appointment JOIN Doctor ON Doctor.DocID = Appointment.DocID WHERE PatientID = %s"""
    Patient = PatientID
    cursor.execute(sql_createView, [Patient])
    conn.commit()
    
    sql_view = ("SELECT * FROM view_Appointment WHERE PatientID = %s")
    cursor.execute(sql_view, [Patient])
    values = cursor.fetchall()
    value = list(values[0])
       
    keys = ['PatientID', 'Doc_FirstName', 'ApptDate', 'Reason']
    zipped = zip(keys, value)
    Appt_view = {}
    Appt_view = {k:v for k, v in zipped}
    conn.rollback()
    conn.close()
    return Appt_view
#Test function
#view_Appointment(172)
#############################################################################################################################


"This block updates Appointment record"
def Update_Appointment(PatientID, NewDocID, NewApptDate):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    Appt_Details = (NewDocID, NewApptDate, PatientID)
    sql_UpdateAppt = ("UPDATE Appointment SET DocID = %s, ApptDate = %s WHERE PatientID = %s")
    cursor.execute(sql_UpdateAppt, Appt_Details)
    conn.commit()
    conn.close()
    
#Test function
#Update_Appointment(172, 'Doc25', '2018-05-31')
#############################################################################################################################


"This block inserts Treatment into treatment record into database"
def InsertTreatment(TreatmentID, Ailment, PrescriptionDate, ExpectedOutcome, warnings):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
    
    sql_Insert = "INSERT INTO treatments (TreatmentID, Ailment, PrescriptionDate, ExpectedOutcome, warnings) VALUES (%s, %s, %s, %s, %s)"
    TreatmentDetails = (TreatmentID, Ailment, PrescriptionDate, ExpectedOutcome, warnings)
    cursor.execute(sql_Insert, TreatmentDetails)
    conn.commit()
    conn.close()
#Test function
#InsertTreatment('802', 'Cactomiosis', '2018-04-25', 'Complicated Emanciation', 'Do not eat for 30days')
##############################################################################################################################


"This block inserts Patient's Bills into Bills record into database"
def InsertBill(PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
    
    sql_Insert = "INSERT INTO Bill (PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate) VALUES (%s, %s, %s, %s, %s, %s)"
    BillDetails = (PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate)
    cursor.execute(sql_Insert, BillDetails)
    conn.commit()
    conn.close()
#Test function
#InsertBill(172, 052, '2018-04-25', 50100, 'Treatment of stomach Pain', '2018-04-27')
##############################################################################################################################
    

"This block creates view of Patient's Bills"
def view_Bill(PatientID):
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Bills AS SELECT PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate 
    FROM Bill WHERE PatientID = %s"""
    Patient = PatientID
    cursor.execute(sql_createView, [Patient])
    conn.commit()
    
    conn.query("SELECT * FROM view_Bills WHERE PatientID = %s" %Patient)
    r = conn.store_result()
    Bills = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Bills
#Test function
#view_Bill(172)
############################################################################################################################

"This block Delete bills of Patientss"
def DeleteBill(BillNumber):
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_DeleteBill = ("DELETE FROM BILL WHERE BillNumber = %s" %BillNumber)
    cursor.execute(sql_DeleteBill)
    conn.commit()
    conn.close()
    
#Test function
DeleteBill('052')
#############################################################################################################################
    

"This block creates view of Doctors"
def view_Doctors():
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Doctors AS SELECT * FROM Doctor"
    cursor.execute(sql_createView)
    conn.commit()
    
    conn.query("SELECT * FROM view_Doctors")
    r = conn.store_result()
    Doctors = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Doctors
#Test function
#view_Doctors()
#############################################################################################################################


"This block creates view of Nurses"
def view_Nurses():
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Nurses AS SELECT * FROM Nurses"
    cursor.execute(sql_createView)
    conn.commit()
    
    conn.query("SELECT * FROM view_Nurses")
    r = conn.store_result()
    Nurses = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Nurses
#Test function
#view_Nurses()
#############################################################################################################################


"This block creates view of Rooms"
def view_Rooms():
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Rooms AS SELECT * FROM Rooms"
    cursor.execute(sql_createView)
    conn.commit()
    
    conn.query("SELECT * FROM view_Rooms")
    r = conn.store_result()
    Rooms = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Rooms
#Test function
#view_Rooms()
#############################################################################################################################


"This block creates view of Employees"
def view_Employees():
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Employees AS SELECT * FROM Employees"
    cursor.execute(sql_createView)
    conn.commit()
    
    conn.query("SELECT * FROM view_Employees")
    r = conn.store_result()
    Employees = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Employees
#Test function
#view_Employees()
#############################################################################################################################


"This block creates view for Departments record"
def view_Departments():
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Department AS SELECT * FROM Department"
    cursor.execute(sql_createView)
    conn.commit()
    
    conn.query("SELECT * FROM view_Department")
    r = conn.store_result()
    Departments = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Departments
#Test function
#view_Departments()  
#############################################################################################################################

'This block inserts view of medical record of a patient'
def view_history(PatientID):
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database!")
    
    try:
        sql_view_history = ("""CREATE OR REPLACE ALGORITHM = MERGE VIEW view_history AS SELECT * FROM treatments join Patient ON PatientID WHERE PatientID = %s""")
        cursor.execute(sql_view_history, [PatientID])
        conn.commit()
    except ViewCreationError:
        print("View Creation failed!")
    
    conn.query("SELECT * FROM view_history")
    r = conn.store_result()
    Patient_history = r.fetch_row(maxrows = 100, how=1)
    
    conn.rollback()
    conn.close()
    return Patient_history
#Test function
view_history(172)
#############################################################################################################################

'This block index the PatientID for ease of search'

def index_patientID():
    
    try:
        import MySQLdb
        conn = MySQLdb.connect(host = "Localhost",
                               user = "root",
                               passwd = "password",
                               db = "Hospital_finaldb")
        cursor = conn.cursor()
    except ConnectionError:
        print("Unable to connect to database")
        
    sql_index = ("CREATE UNIQUE INDEX index_patientID ON Patient (PatientID)")
    cursor.execute(sql_index)
    conn.commit()
    conn.close()
#############################################################################################################################