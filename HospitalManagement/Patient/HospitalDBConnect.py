# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:42:10 2018

@author: Thinkpad
"""

##########################################################################################################################

'This block inserts Patient record into database'


def InsertPatient(PatientID, First_Name, Last_Name, PhoneNumber, Address):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_Insert = "INSERT INTO patient (PatientID, FirstName, LastName, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
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
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
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
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
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
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
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
    if len(values) > 0:
        value = list(values[0])
        keys = ['PatientID', 'Doc_FirstName', 'ApptDate', 'Reason']
        zipped = zip(keys, value)
        Appt_view = {}
        Appt_view = {k: v for k, v in zipped}
        conn.rollback()
        conn.close()
        return Appt_view
    else: return {}


#Test function
#view_Appointment(172)

###########################################################################################################################
"This block creates view of Patient's appointments"
# Sonwoo 

def view_Appointments_patient(PatientID):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Appointment AS SELECT *
    FROM Appointment WHERE PatientID = %s"""
    Patient = PatientID
    cursor.execute(sql_createView, [Patient])
    conn.commit()

    sql_view = ("SELECT * FROM view_Appointment WHERE PatientID = %s")
    cursor.execute(sql_view, [Patient])
    r = cursor.fetchall()
    if len(r) > 0:
        conn.rollback()
        conn.close()
        return r
    else: return {}


#Test function
#view_Appointment(172)

###########################################################################################################################

"This block creates view of Patient's appointments with doctors"


def view_Treatment(PatientID):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Treatment AS SELECT Ailment, Warnings, PatientID, DocID, Treatments.TreatmentID, ExpectedOutcome, PrescriptionDate
    FROM treat JOIN Treatments ON treat.TreatmentID = Treatments.TreatmentID WHERE PatientID = %s"""
    Patient = PatientID
    cursor.execute(sql_createView, [Patient])
    conn.commit()

    sql_view = ("SELECT * FROM view_Treatment WHERE PatientID = %s")
    cursor.execute(sql_view, [Patient])
    r = cursor.fetchall()
    # values = cursor.fetchall()
    # value = list(values[0])

    # keys = ['Ailment', 'Warnings', 'PatientID', 'DocID', 'TreatmentID', 'ExpectedOutcome', 'PrescriptionDate']
    # zipped = zip(keys, value)
    # treatment_view = {}
    # treatment_view = {k: v for k, v in zipped}
    # conn.rollback()
    # conn.close()
    return r


#Test function
#view_Treatment(101)
#############################################################################################################################

"This block updates Appointment record"


def Update_Appointment(PatientID, NewDocID, NewApptDate):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    Appt_Details = (NewDocID, NewApptDate, PatientID)
    sql_UpdateAppt = (
        "UPDATE Appointment SET DocID = %s, ApptDate = %s WHERE PatientID = %s"
    )
    cursor.execute(sql_UpdateAppt, Appt_Details)
    conn.commit()
    conn.close()


#Test function
#Update_Appointment(172, 'Doc25', '2018-05-31')
#############################################################################################################################
''' shows all appointments '''


def view_Appointments():
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Appointment AS SELECT * FROM Appointment"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Appointment")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


"This block inserts Treatment into treatment record into database"


def InsertTreatment(TreatmentID, Ailment, PrescriptionDate, ExpectedOutcome,
                    warnings):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_Insert = "INSERT INTO treatments (TreatmentID, Ailment, PrescriptionDate, ExpectedOutcome, warnings) VALUES (%s, %s, %s, %s, %s)"
    TreatmentDetails = (TreatmentID, Ailment, PrescriptionDate,
                        ExpectedOutcome, warnings)
    cursor.execute(sql_Insert, TreatmentDetails)
    conn.commit()
    conn.close()


#Test function
#InsertTreatment('802', 'Cactomiosis', '2018-04-25', 'Complicated Emanciation', 'Do not eat for 30days')
##############################################################################################################################

"This block inserts Patient's Bills into Bills record into database"


def InsertBill(PatientID, BillNumber, ReleaseDate, Amount, Description,
               DueDate):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_Insert = "INSERT INTO Bill (PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate) VALUES (%s, %s, %s, %s, %s, %s)"
    BillDetails = (PatientID, BillNumber, ReleaseDate, Amount, Description,
                   DueDate)
    cursor.execute(sql_Insert, BillDetails)
    conn.commit()
    conn.close()


#Test function
#InsertBill(172, 052, '2018-04-25', 50100, 'Treatment of stomach Pain', '2018-04-27')
##############################################################################################################################

"This block creates view of Patient's Bills"


def view_Bill(PatientID):

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Bills AS SELECT PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate
    FROM Bill WHERE PatientID = %s"""
    Patient = PatientID
    cursor.execute(sql_createView, [Patient])
    conn.commit()

    cursor.execute("SELECT * FROM view_Bills WHERE PatientID = %s" % Patient)
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Bill(172)
############################################################################################################################
def view_Bill_more(BillNumber):

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Bills AS SELECT PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate
    FROM Bill WHERE BillNumber = %s"""
    cursor.execute(sql_createView, [BillNumber])
    conn.commit()

    cursor.execute("SELECT * FROM view_Bills WHERE BillNumber = %s" % BillNumber)
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Bill(172)
############################################################################################################################

def view_Treatment_more(treatmentNumber):

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_treatment_more AS SELECT Ailment, Warnings, PatientID, DocID, Treatments.TreatmentID, ExpectedOutcome, PrescriptionDate
    FROM treat JOIN Treatments ON treat.TreatmentID = Treatments.TreatmentID WHERE treat.TreatmentID = %s"""
    cursor.execute(sql_createView, [treatmentNumber])
    conn.commit()

    cursor.execute("SELECT * FROM view_treatment_more WHERE TreatmentID = %s" % treatmentNumber)
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Bill(172)
############################################################################################################################


"This block Delete bills of Patientss"


def DeleteBill(BillNumber):
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_DeleteBill = ("DELETE FROM BILL WHERE BillNumber = %s" % BillNumber)
    cursor.execute(sql_DeleteBill)
    conn.commit()
    conn.close()


#Test function
#DeleteBill('052')
#############################################################################################################################

"This block creates view of Doctors"


def view_Doctors():
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Doctors AS SELECT * FROM Doctor"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Doctors")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Doctors()
#############################################################################################################################
'''Creates a list of bills '''


def view_Bills():
    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Bills AS SELECT * FROM Bill"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Bills")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


"This block creates view of Nurses"


def view_Nurses():

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Nurses AS SELECT * FROM Nurses"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Nurses")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Nurses()
#############################################################################################################################

"This block creates view of Rooms"


def view_Rooms():

    try:
        import pymysql.cursors
        #import _mysql
        conn = pymysql.connect(
            host="localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Rooms AS SELECT * FROM Rooms"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Rooms")
    cursor.execute("SELECT * FROM view_Rooms")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Rooms()
#############################################################################################################################

"This block creates view of Employees"


def view_Employees():

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Employees AS SELECT * FROM Employees"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Employees")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


''' shows all patients '''


def view_Patients():

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Patient AS SELECT * FROM patient"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Patient")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Employees()
#############################################################################################################################

"This block creates view for Departments record"


def view_Departments():

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_createView = "CREATE OR REPLACE ALGORITHM = MERGE VIEW view_Department AS SELECT * FROM Department"
    cursor.execute(sql_createView)
    conn.commit()

    cursor.execute("SELECT * FROM view_Department")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
#view_Departments()
#############################################################################################################################

'This block inserts view of medical record of a patient'


def view_history(PatientID):

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database!")

    sql_view_history = (
        """CREATE OR REPLACE ALGORITHM = MERGE VIEW view_history AS SELECT * FROM Treatments join patient ON PatientID WHERE PatientID = %s"""
    )
    cursor.execute(sql_view_history, [PatientID])
    conn.commit()

    cursor.execute("SELECT * FROM view_history")
    r = cursor.fetchall()

    conn.rollback()
    conn.close()
    return r


#Test function
# view_history(172)
#############################################################################################################################

'This block index the PatientID for ease of search'


def index_patientID():

    try:
        import pymysql.cursors
        conn = pymysql.connect(
            host="Localhost", user="root", passwd="pass", db="Hospital")
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    except ConnectionError:
        print("Unable to connect to database")

    sql_index = ("CREATE UNIQUE INDEX index_patientID ON Patient (PatientID)")
    cursor.execute(sql_index)
    conn.commit()
    conn.close()


#############################################################################################################################
