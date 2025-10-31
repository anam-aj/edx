# Program to convert mass into energy

def main():

    # Promts user for mass
    mass = int(input("Mass: "))

    # Convert mass to energy
    c = 3 * 10**8
    energy = mass * c**2

    # Prints to user
    print(energy)


main()
