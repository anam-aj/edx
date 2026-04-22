CREATE DATABASE StudentExamSystem;
USE StudentExamSystem;

-- Table 1: Student
CREATE TABLE Student (
    StudentID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    ProgrammeCode VARCHAR(10) NOT NULL,
    DateOfEnrolment DATE NOT NULL
);

-- Table 2: FeePaid
CREATE TABLE FeePaid (
    StudentID VARCHAR(20),
    Semester INT NOT NULL,
    dateofPayment DATE NOT NULL,
    AmountPaid DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID) ON DELETE CASCADE
);
