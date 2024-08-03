    # TODO: Find longest match of each STR in DNA sequence
    key_list = list(list_persons[0].keys())
    cpy_list = key_list
    STR_list = cpy_list.pop(0)

    match_dict = {}
    for STR in STR_list:
        match_dict[STR] = longest_match(dna_sequence, STR)

    # TODO: Check database for matching profiles
    for i in range(len(list_persons)):
        count = 0
        for j in range(len(STR_list)):
            count += 1
            if list_persons[i][STR_list[j]] != match_dict[STR_list[j]]:
                break
        if count == len(STR_list):
            print(list_persons[i][key_list[0]])
            return

    print("No match")
    return
