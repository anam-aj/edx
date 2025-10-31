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

