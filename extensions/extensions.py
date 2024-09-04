# Program to find media type of file

def main():

    # Promts user for filename
    file = input("File name: ")

    # Check extension and tell media type
    media_type = check_type(file)

    # Prints media type to user
    print(media_type)

def check_type(file_name):
    
