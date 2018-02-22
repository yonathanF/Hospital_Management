DROP database IF EXISTS Hospital; 
Create database Hospital;
use Hospital; 

CREATE TABLE Patient(
    PatientID int NOT NULL PRIMARY KEY, 
    DepartmentID int, 
    RoomNumber int,
    NurseID int,
    BillID int,  
    DocID varchar(10), 
    TreatmentID int, 
    FirstName varchar(100),  
    LastName varchar(100),
    Phone char(11), 
    City varchar(20), 
    State char(2), 
    Street varchar(50), 
    ZipCode char(5)
);

CREATE TABLE Employees(
    EmployeeID int primary key,
    FirstName varchar(50),  
    LastName varchar(50), 
    Address varchar(200),
    Phone char(11),
    Responsibilities varchar(1024), 
    EmploymentDate date,
    Email varchar(100),
    Salary numeric(12,2)
);

CREATE TABLE Nurses(
    NurseID int NOT NULL PRIMARY KEY,
    PatientID int, 
    FirstName varchar(50),
    LastName varchar(50), 
    Phone char(11),
    Address varchar(100),
    Speciality varchar(1024),
    Email varchar(100),
    Salary numeric(12,2)
); 

CREATE TABLE Rooms(
    PatientID int,  
    DepartmentID int, 
    RoomNumber int NOT NULL primary key, 
    Capacity int
);

CREATE TABLE Doctor(
    DocID    varchar(10) NOT NULL PRIMARY KEY,
    PatientID int,  
    FirstName varchar(20),
    LastName varchar(20),
    Address varchar(200),
    Phone char(11),
    Email varchar(100),
    Salary numeric(12,2)
); 

CREATE TABLE Drug(
    DrugID int primary key,
    TreatmentID int, 
    MfgDate date,
    BrandName varchar(30),
    ExpDate date,
    DrugName varchar(255), 
    SideEffects varchar(1024), 
    Description varchar(1024),
    Dosage varchar(255)
); 

CREATE TABLE Bill(
    PatientID int,
    BillNumber int primary key, 
    ReleaseDate date,
    Amount numeric(12,2), 
    Description varchar(1024),
    DueDate date
);

CREATE TABLE Treatments(
    PatientID int,
    TreatmentID int primary key, 
    Ailment varchar(1024),
    PrescriptionDate date, 
    ExpectedOutcome varchar(1024), 
    Warnings varchar(1024)
);

CREATE TABLE Department(
    DepartmentID int primary key,
    DeptName varchar(50), 
    DeptHead varchar(50),
    DeptDesc varchar(1024)
);

CREATE TABLE appointment(
    DocID int references Doctor (DocID),
    PatientID int references Patient (PatientID),
    ApptDate date,
    primary key(DocID, PatientID)
);

CREATE TABLE serves(
    RoomNumber int references Room (RoomNumber),
    EmployeeID int references Employee (EmployeeID),
    primary key (RoomNumber, EmployeeID)
);

CREATE TABLE admitted_to(
    PatientID int references Patient (PatientID),
    DID int references Department (DID),
    primary key (PatientID, DID) 
);

ALTER TABLE Patient
ADD foreign key (DepartmentID) references Department(DepartmentID) on delete restrict;

ALTER TABLE Patient
ADD foreign key (RoomNumber) references Rooms(RoomNumber) on delete restrict;

ALTER TABLE Patient
ADD foreign key (NurseID) references Nurses(NurseID) on delete restrict;

ALTER TABLE Patient
ADD foreign key (DocID) references Doctor(DocID) on delete cascade;

ALTER TABLE Patient
ADD foreign key (TreatmentID) references Treatments(TreatmentID) on delete cascade;

ALTER TABLE Patient
ADD foreign key (BillID) references Bill(BillNumber) on delete cascade;

ALTER TABLE Nurses
ADD CONSTRAINT fk_PatientNurses
FOREIGN KEY (PatientID) References Patient(PatientID) ON DELETE RESTRICT;

ALTER TABLE Doctor
ADD foreign key (PatientID) references Patient (PatientID) on delete cascade;

ALTER TABLE Rooms
ADD foreign key (DepartmentID) references Department(DepartmentID)on delete cascade;

ALTER TABLE Rooms
ADD foreign key (PatientID) references Patient(PatientID) on delete cascade;

ALTER TABLE Drug
add foreign key(TreatmentID) references Treatments(TreatmentID) on delete cascade;

ALTER TABLE Bill
ADD foreign key(PatientID) references Patient(PatientID) on delete cascade;

ALTER TABLE Treatments
ADD foreign key(PatientID) references Patient(PatientID) on delete cascade;

