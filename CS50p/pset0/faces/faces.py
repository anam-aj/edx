# Program to replace emoticon with emoji

def main():

    # Promts user for input
    user_input = input("Please type your sentence here: ")

    # Replace emoticon with emoji
    output = user_input.replace(":)", "🙂")
    output = output.replace(":(", "🙁")

    # Prints to user
    print(output)


main()
