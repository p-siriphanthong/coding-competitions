# Running: `python consistency_chapter_2.py [sample | validation | final]`

"""
Sameple Input Case #4: FOXEN

E -> W
F -> E -> W
F -> N -> I
F -> N -> X
N -> I
N -> X -> W
O -> E -> W
O -> I
X -> W

replacements:
{
    E: { E: 0, W: 1 },
    F: { F: 0, E: 1, N: 1, I: 2, X: 2, W: 2 },
    N: { N: 0, I: 1, X: 1, W: 2 },
    O: { O: 0, E: 1, I: 1 W: 2 },
    X: { X: 0, W: 1 },
}
"""

import sys

file_name = sys.argv[1]
input_file = open("Test Cases/{}_input.txt".format(file_name), "r")
output_file = open("Test Cases/{}_output.txt".format(file_name), "w")

input = input_file.read().splitlines()
T = int(input.pop(0))


def updateReplacements(replacements, A, B):
    if A not in replacements:
        replacements[A] = {}
    replacements[A][B] = 1

    if B in replacements:
        for key, count in replacements[B].items():
            if key in replacements[A]:
                replacements[A][key] = min(
                    replacements[A][key], count + 1)
            else:
                replacements[A][key] = count + 1

    for key, value in replacements.items():
        if A not in value:
            continue
        a_count = value[A]
        for subkey, count in replacements[A].items():
            if subkey in value:
                replacements[key][subkey] = min(
                    replacements[key][subkey], a_count + count)
            else:
                replacements[key][subkey] = a_count + count

    return replacements


for t in range(T):
    S = input.pop(0)
    K = int(input.pop(0))

    if K != 0:
        flagment = {}
        replacements = {}
        posible_consistent_chars = set()
        consistent = (None, sys.maxint)

        for ch in S:
            flagment[ch] = 1 if ch not in flagment else flagment[ch] + 1
            replacements[ch] = {ch: 0}

        for _ in range(K):
            [A, B] = input.pop(0)
            posible_consistent_chars.add(A)
            posible_consistent_chars.add(B)
            replacements = updateReplacements(replacements, A, B)
        replacements = {key: replacements[key] for key in S}

        for consistent_char in posible_consistent_chars:
            sum = 0
            is_valid = True
            for key, value in replacements.items():
                if consistent_char not in value:
                    is_valid = False
                    break
                sum += flagment[key] * value[consistent_char]
            if is_valid and sum < consistent[1]:
                consistent = (consistent_char, sum)

        output = "Case #{}: {}".format(
            t + 1, -1 if consistent[0] == None else consistent[1])

    else:
        output = "Case #{}: 0".format(t + 1)

    output_file.write("{}\n".format(output))
    print(output)

input_file.close()
output_file.close()
