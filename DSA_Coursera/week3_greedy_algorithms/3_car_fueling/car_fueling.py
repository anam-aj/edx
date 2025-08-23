from sys import stdin


def min_refills(distance, tank, stops):

    d = distance
    m = tank


    stops = [0] + stops + [d]   # add start and destination
    refills = 0
    current = 0   # index of last refill

    for i in range(1, len(stops)):


    return num_refills




    '''stops = list(stops)
    refills = 0

    if tank >= distance:
        return 0

    if len(stops) == 0:
        return -1

    if len(stops) == 1:
        if tank < stops[0]:
            return -1
        elif (distance - stops[0]) > tank:
            return -1
        else:
            return 1


    for i in range(len(stops)):

        curr_stop = stops[i]
        next_stop = stops[i]
        if next_stop <= tank:
            continue

        curr_stop = stops[i - 1]


        if next_stop > tank:
            return -1

        refills += 1







    stops = list(stops)

    while range_of_car < distance:

        if len(stops) == 0:
            return -1
        next_stop = stops.pop(0)

        if next_stop > range_of_car:
            return -1

        while len(stops) != 0 and next_stop <= range_of_car:
            next_stop = stops.pop(0)

        range_of_car += tank
        refills += 1

        return refills'''


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
