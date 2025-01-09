# Library Management System Database

By ANAM ZAHID


Video overview: <URL HERE>


## Scope

This Library Management System (LMS) database schema is designed to efficiently manage various aspects of a library, including user data, book information, authors, publishers, transactions (borrows and returns), and the availability status of books.As such, included in the database's scope is:

* Users, including both member and staff with baisc identifying information.
* Authors, including basic idenitfying information.
* Publishers, including name and some description.
* Books, including associated relevant information like author, publisher, genre etc.

Out of the scope are borrowing charge, fine, due date, borrowing rules.


## Functional Requirements

This database will support:

* CRUD operations for users, books, authors and publishers.
* Availability status of books.
* Keep track of borrowed books, date and the user who borrowed.


## Representation

Entities are captured in MYSQL tables with the following schema.

### Entities

The database includes the following entities:

* Which entities will you choose to represent in your database?
* What attributes will those entities have?
* Why did you choose the types you did?
* Why did you choose the constraints you did?

### Relationships

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

## Optimizations

In this section you should answer the following questions:

* Which optimizations (e.g., indexes, views) did you create? Why?

## Limitations

In this section you should answer the following questions:

* What are the limitations of your design?
* What might your database not be able to represent very well?
