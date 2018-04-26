
ALTER TABLE Bill MODIFY BillNumber INTEGER NOT NULL AUTO_INCREMENT;
ALTER TABLE Treatments MODIFY TreatmentID INTEGER NOT NULL AUTO_INCREMENT;

select * from patient where PatientID = 101; 
SELECT * FROM Treatments join patient ON PatientID WHERE PatientID = 101;

SELECT count(PatientID) from Appointment where ApptDate = CURDATE(); 
SELECT DISTINCT count(DocID)  from Doctor; 
SELECT DISTINCT count(RoomNumber)  from Rooms; 

select distinct FirstName, LastName, RoomNumber, Capacity, DeptName
from (Rooms join patient on Rooms.PatientID=patient.PatientID) join Department  
on Department.DID=Rooms.DepartmentID;



SELECT patient.PatientID, patient.FirstName as FirstName, patient.LastName as LastName, 
Doctor.FirstName as docFirst, Doctor.LastName as docLast, ApptDate, Reason 
FROM (Appointment JOIN Doctor ON Doctor.DocID = Appointment.DocID) JOIN patient on Appointment.PatientID = patient.PatientID

select patient.PatientID, BillNumber, ReleaseDate, Amount, Description, DueDate, FirstName, LastName from Bill join patient on patient.PatientID=Bill.PatientID;

select patient.PatientID, FirstName, LastName, Phone, Address, ApptDate
from patient left join Appointment on patient.PatientID = Appointment.PatientID;

delete from Treatments;

INSERT INTO Treatments(TreatmentID,Ailment,PrescriptionDate,ExpectedOutcome,Warnings) VALUES (11,'Allergies',NULL,'This is the expected outcome for Allergies traetment ','This is warning for treatment 11');
