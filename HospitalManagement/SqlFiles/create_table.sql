DROP database IF EXISTS Hospital; 

Create database Hospital; 

use Hospital; 

CREATE TABLE patient( 
PatientID int NOT NULL PRIMARY KEY, 
FirstName varchar(100), 
LastName varchar(100), 
Phone char(15), 
Address varchar(200) ); 

CREATE TABLE Employees( 
EmployeeID int primary key, 
FirstName varchar(50), 
LastName varchar(50), 
Address varchar(200), 
Phone char(11), 
Responsibilities varchar(1024), 
EmploymentDate date, 
Email varchar(100), 
Salary numeric(12,2) ); 

CREATE TABLE Nurses( 
NurseID int NOT NULL PRIMARY KEY, 
FirstName varchar(50), 
LastName varchar(50), 
Phone char(11), 
Address varchar(100),
 Speciality varchar(1024),
 Email varchar(100),
 Salary numeric(12,2) ); 

CREATE TABLE Rooms( 
PatientID int, 
DepartmentID int, 
RoomNumber int NOT NULL primary key, 
Capacity int ); 

CREATE TABLE Doctor( 
DocID varchar(10) NOT NULL PRIMARY KEY, 
FirstName varchar(20), 
LastName varchar(20), 
Address varchar(200), 
Phone char(15), 
Email varchar(100), 
Salary numeric(12,2) ); 


CREATE TABLE Bill( 
PatientID int, 
BillNumber int primary key, 
ReleaseDate date, 
Amount numeric(12,2), 
Description varchar(1024), 
DueDate date ); 

CREATE TABLE Treatments( 
TreatmentID int primary key, 
Ailment varchar(1024), 
PrescriptionDate date, 
ExpectedOutcome varchar(1024), 
Warnings varchar(1024) ); 

CREATE TABLE Department( 
DID int primary key, 
DeptName varchar(50), 
DeptHead varchar(50), 
DeptDesc varchar(1024) ); 


CREATE TABLE serves( 
RoomNumber int references Room (RoomNumber), 
EmployeeID int references Employee (EmployeeID), 
primary key (RoomNumber, EmployeeID) ); 

CREATE TABLE admitted_to( 
PatientID int references Patient (PatientID), 
DID int references Department (DID), 
primary key (PatientID, DID) ); 

CREATE TABLE supports( 
PatientID int references Patient (PatientID), 
NurseID int references Nurses (NurseID), 
primary key (PatientID, NurseID) ); 

CREATE TABLE used_for( 
TreatmentID int references Treatments (TreatmentID),
DrugID int references Drug (DrugID), 
primary key (TreatmentID, DrugID) ); 

CREATE TABLE treat( 
PatientID int references Patient (PatientID),
DocID varchar(10) references Doctor (DocID),  
TreatmentID int references Treatments (TreatmentID),
primary key (PatientID, TreatmentID, DocID) ); 

CREATE TABLE Appointment( 
PatientID int references Patient (PatientID), 
DocID varchar(10) references Doctor (DocID), 
ApptDate date, 
Reason varchar(1000),
primary key (PatientID, DocID) ); 


ALTER TABLE Rooms ADD foreign key (DepartmentID) references Department(DID)on delete cascade; 

ALTER TABLE Rooms ADD foreign key (PatientID) references Patient(PatientID) on delete cascade; 

ALTER TABLE Bill ADD foreign key(PatientID) references Patient(PatientID) on delete cascade; 


