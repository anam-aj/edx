import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Please provide proper command-line arguments")
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        dict_file = csv.DictReader(file)
        list_persons = list(dict_file)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna_sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    # List of keys
    key_list = list(list_persons[1].keys())

    # List of STR
    STR_list = list(key_list)
    STR_list.pop(0)

    # Dictionary of longest match of each STR
    match_dict = {}
    for STR in STR_list:
        match_dict[STR] = longest_match(dna_sequence, STR)

    # TODO: Check database for matching profiles
    # Loop through each person given in database
    for i in range(len(list_persons)):

        # Variable to count the no of matching STR
        count = 0

        # Loop through each STR of one person and compare with longest_match
        for j in range(len(STR_list)):
            if int(list_persons[i][STR_list[j]]) != int(match_dict[STR_list[j]]):
                break
            count += 1

        # Prints winner if all STR match
        if count == len(STR_list):
            print(list_persons[i][key_list[0]])
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
