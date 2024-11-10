# MyNotes web app

A web app to make notes.


### Video Demo:


### PIP install libraries:

cs50
Flask
Flask-Session
requests


### Description:

A Flask app that allows user to store Notes online. It provides user the option to add and delete notes. Initially user is greeted with a login page. Login credentials are stored in SQL database. For unregistered user there is an option given the login page itself. After successfully logging in user is taken to home page where all user notes are dispalyed as nice formatted cards. Also user is provided with menu of options namely "Home", "AddNote", "RemoveNote" upon clicking which user is taken to the respective pages.

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

Description of the above mentioned is as follows:

* #### savedfiles:

    * Notes created by user are saved here. Saved files are created using "user_id" as name of file which is unique for every user.

* #### static:

    * Contains images and the CSS file for styling the pages.

* #### templates:

    * Contains the HTML templates used in the project namely:

        * addnote.html
        * index.html
        * layout.html
        * 
