# Program to answer the "Great question of life"

# Promts user for answer
answer = input("What is the answer to Great Question of Life? ")

# Check answer
if int(answer) == 42:
    print("Yes")
elif answer.lower().strip == "forty two" or answer.lower().strip == "forty-two":
    print("Yes")
else:
    print("No")
