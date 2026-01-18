# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    multiplier = 263
    prime = 1000000007

    pattern_hash = hash_string(pattern, multiplier, prime)
    substring_hashes = compute_hashes(text, pattern, multiplier, prime)

    positions = []

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == substring_hashes[i]:
            substring = text[i: (i + len(pattern))]
            if substring == pattern:
                positions.append(i)

    return positions


def hash_string(s, multiplier, prime):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def compute_hashes(text, pattern, multiplier, prime):
    substring_hashes = [None] * (len(text) - len(pattern) + 1)
    last_substring = text[len(text) - len(pattern): ]
    substring_hashes[-1] = hash_string(last_substring, multiplier, prime)

    y = 1
    for i in range(len(pattern)):
        y = (y * multiplier) % prime

    for i in range(len(substring_hashes) - 2, -1, -1):
        substring_hashes[i] = ((multiplier * substring_hashes[i + 1]) + ord(text[i]) - (y * ord(text[i + len(pattern)]))) % prime

    return substring_hashes


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
