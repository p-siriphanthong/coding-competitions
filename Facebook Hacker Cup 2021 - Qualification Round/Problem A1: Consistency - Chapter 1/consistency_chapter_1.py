# Running: `python consistency_chapter_1.py [sample | validation | final]`

import sys

VOWELS = ["A", "E", "I", "O", "U"]

file_name = sys.argv[1]
input_file = open("Test Cases/{}_input.txt".format(file_name), "r")
output_file = open("Test Cases/{}_output.txt".format(file_name), "w")

input = input_file.read().splitlines()
T = int(input.pop(0))


def check_consistency(string):
    return len(list(set(string))) == 1


def count_chars(string):
    count = {}
    for ch in string:
        count[ch] = count[ch] + 1 if ch in count else 1
    return count


def is_vowel(ch):
    return ch in VOWELS


def get_replace_time(string, replace_with):
    time = 0
    is_replace_with_vowel = is_vowel(replace_with)
    for ch in string:
        if ch == replace_with:
            continue
        time += 2 if is_replace_with_vowel == is_vowel(ch) else 1
    return time


for t in range(T):
    S = input.pop(0)
    count = count_chars(S)

    # case 1: vowel consistency string
    vowel_count = {k: v for k, v in count.items() if k in VOWELS}
    if len(vowel_count) == 0:
        time_1 = len(S)
    else:
        ch = max(vowel_count, key=lambda k: vowel_count.get(k))
        time_1 = get_replace_time(S, ch)

    # case 2: consonant consistency string
    consonant_count = {k: v for k, v in count.items() if k not in VOWELS}
    if len(consonant_count) == 0:
        time_2 = len(S)
    else:
        ch = max(consonant_count, key=lambda k: consonant_count.get(k))
        time_2 = get_replace_time(S, ch)

    min_time = 0 if check_consistency(S) else min(time_1, time_2)

    output = "Case #{}: {}".format(t + 1, min_time)
    output_file.write("{}\n".format(output))
    print(output)

input_file.close()
output_file.close()
