# Program to check validity of email address

import validators


def main():

    # Ask user for email
    email = input("Email: ")

    # Check validity and print status
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
