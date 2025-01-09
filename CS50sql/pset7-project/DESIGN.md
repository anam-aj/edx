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

Information is captured in MYSQL database with the following schema.

### Entities

The database includes the following entities:

#### 1. Users

The `users` table contains the following columns

* `id`: A unique identifier for each user (auto-incremented).
* `first_name`: User's first name (non-nullable).
* `last_name`: User's last name (non-nullable).
* `email`: User's email address (non-nullable and unique).
* `phone_number`: User's phone number (non-nullable).
* `address`: User's address (optional).
* `role`: Specifies if the user is a 'member' or 'staff' (non-nullable).

#### 2. Authors

The `authors` table contains the following columns

* `id`: A unique identifier for each author (auto-incremented).
* `name`: The name of the author (non-nullable).
* `birth_year`: The birth year of the author (optional).
* `bio`: A short biography of the author (optional).

#### 3. Publishers

The `publishers` table contains the following columns

* `id`: A unique identifier for each publisher (auto-incremented).
* `name`: The name of the publisher (non-nullable).
* `bio`: A short biography of the publisher (optional).

#### 4. Books

The `books` table contains the following columns

* `id`: A unique identifier for each book (auto-incremented).
* `title`: The title of the book (non-nullable).
* `author_id`: Foreign key referencing the authors table.
* `publisher_id`: Foreign key referencing the publishers table.
* `publication_year`: The year the book was published (optional).
* `genre`: The genre of the book (optional).
* `availability_status`: The availability of the book, either 'available' or 'not_available' (default is 'available').


#### 5. Borrowing Transactions Table

The `borrowing_transactions` table contains the following columns

* `id`: A unique identifier for each transaction (auto-incremented).
* `user_id`: Foreign key referencing the users table.
* `book_id`: Foreign key referencing the books table.
* `date_time`: The date and time of the transaction (default is the current timestamp).
* `action`: The action performed, either 'Borrowed' or 'Returned' (non-nullable).

### Triggers

#### book_status_update
* The `book_status_update` trigger automatically updates the availability status of books in the books table when a borrow or return transaction is recorded in the `borrowing_transactions` table. After Insert, whenever a new row is inserted into the `borrowing_transactions` table, this trigger checks the action field: If the action is 'Borrowed', the availability status of the corresponding book is set to 'not_available'. If the action is 'Returned', the availability status is set to 'available'.


### Relationships

In this section you should include your entity relationship diagram and describe the relationships between the entities in your database.

## Optimizations

In this section you should answer the following questions:

* Which optimizations (e.g., indexes, views) did you create? Why?

## Limitations

In this section you should answer the following questions:

* What are the limitations of your design?
* What might your database not be able to represent very well?
