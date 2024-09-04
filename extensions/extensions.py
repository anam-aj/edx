# Program to find media type of file

def main():

    # Promts user for filename
    file = input("File name: ")

    # Check extension and tell media type
    media_type = check_type(file)

    # Prints media type to user
    print(media_type)

def check_type(file_name):

    if file_name.endswith(".gif"):
        print("image/gif")

    elif file_name.endswith(".jpg"):
        print("image/jpeg")

    elif file_name.endswith(".jpeg"):
        print("image/jpeg")

    elif file_name.endswith(".png"):
        print("image/png")

    elif file_name.endswith(".pdf"):
        print("image/gif")

    elif file_name.endswith(".txt"):
        print("image/gif")

    elif file_name.endswith(".zip"):
        print("image/gif")

    else:
        print("application/octet-stream")

