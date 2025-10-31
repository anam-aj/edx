from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    sorted_segments = sorted(segments, key=lambda s: s.end)

    first_point = sorted_segments[0].end
    points.append(first_point)

    for s in sorted_segments:
        if first_point < s.start:
            points.append(s.end)
            first_point = s.end

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
