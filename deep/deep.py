# Program to answer the "Great question of life"

# Promts user for answer
answer = input("What is the answer to Great Question of Life? ")

# Strip spaces and converts to lowercase
answer = answer.lower().strip()

# Check answer
if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("yes")
elif answer == "forty-two":
    print("Yes")
else:
    print("No")
