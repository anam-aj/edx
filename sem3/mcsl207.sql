CREATE TABLE Member (
    memberId CHAR(4) PRIMARY KEY,
    memberName VARCHAR(50),
    memberAddress VARCHAR(100),
    memberPhone VARCHAR(15)
);

CREATE TABLE Book (
    BookId CHAR(4) PRIMARY KEY,
    BookTitle VARCHAR(100),
    FirstAuthor VARCHAR(50)
);

CREATE TABLE BookIssued (
    memberID CHAR(4),
    BookID CHAR(4),
    IssueDate DATE,
    returnDate DATE,
    PRIMARY KEY(memberID, BookID),
    FOREIGN KEY(memberID) REFERENCES Member(memberId),
    FOREIGN KEY(BookID) REFERENCES Book(BookId)
);

INSERT INTO Member VALUES
('0001', 'Alice', 'Delhi', '12345'),
('0002', 'Bob', 'Mumbai', '67890'),
('0003', 'Charlie', 'Kolkata', '54321'),
('0004', 'David', 'Chennai', '12345'),
('0005', 'Eve', 'Bangalore', '98765');
