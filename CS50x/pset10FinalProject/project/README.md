# MyNotes web app

This is a web application that allows users to register, log in, and manage their personal notes. Users can add, view, and remove notes.


### Video Demo:


### Description:

A Flask app that allows user to store Notes online. It provides user the option to add and delete notes. Initially user is greeted with a login page. Login credentials are stored in SQL database. For unregistered user there is an option to register themselves given at the login page itself. After successfully logging in user is taken to home page where all user notes are dispalyed as nice formatted cards. Also user is provided with menu of options namely "Home", "AddNote", "RemoveNote" upon clicking which user is taken to the respective pages.

* #### Features
    * User registration and login
    * Password hashing for security
    * Session management
    * Add, view, and remove notes

* #### Technologies Used
    * Python
    * Flask
    * SQLite
    * CS50 Library
    * Werkzeug for password hashing

* #### Usage
    * Register a new user account.
    * Log in with your credentials.
    * Add, view, and remove notes.

* #### PIP install libraries:
    * cs50
    * Flask
    * Flask-Session
    * requests

* #### File Structure
    * app.py: Main application file.
    * templates/: HTML templates for rendering web pages.
    * helpers.py: Helper functions for managing notes and user sessions.

### Detailed description of project Structure and Code
Root directory is named "project" and it contains the following files and folders:

* #### Folders
    * savedfiles
    * static
    * templates

* #### Files
    * app.py
    * helpers.py
    * README.md
    * requirements.txt
    * users.db

#### Description of the above mentioned is as follows:

* #### savedfiles:

    * Notes created by user are saved here. Saved files are created using "user_id" as name of save_file which is unique for every user.

* #### static:

    * Contains images and the CSS file for styling the pages.

* #### templates:

    * Contains the HTML templates used in the project as given below where "layout.html" is the main template and all other templates extends this using jinja:

        * ##### addnote.html

            * Contains two input fields 'title' and 'detail' and a button 'addnote' which submits the details entered by user to the route "/addnote".

        * ##### index.html

            * Loops through the user's note's dictionary and dynamically generate and displays the information formatted as cards.

        * ##### layout.html

            * Parent template that contains the basic structure of all the webpages. Bootstraps the webpages and also includes meta tag to make webpages look good on small screen devices like mobile phone.

        * ##### login.html

             * Hosts to input field namely 'username' and 'password' and a submit button named 'login'.

        * ##### register.html
        * ##### removenote.html
