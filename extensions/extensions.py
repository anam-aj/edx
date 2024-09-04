# Program to find media type of file


def main():

    # Promts user for filename
    file = input("File name: ")

    # Strip spaces and converts to lowercase
    file = file.lower().strip()

    # Get media type
    media_type = get_media_type(file)

    # Prints media type to user
    print(media_type)


def get_media_type(file_name):

    if file_name.endswith(".gif"):
        return ("image/gif")

    elif file_name.endswith(".jpg"):
        return ("image/jpeg")

    elif file_name.endswith(".jpeg"):
        return ("image/jpeg")

    elif file_name.endswith(".png"):
        return ("image/png")

    elif file_name.endswith(".pdf"):
        return ("application/pdf")

    elif file_name.endswith(".txt"):
        return ("text/plain")

    elif file_name.endswith(".zip"):
        return ("application/zip")

    else:
        return ("application/octet-stream")


main()
