# Running: `python xs_and_os.py [sample | validation | final]`

import sys

file_name = sys.argv[1]
input_file = open("Test Cases/{}_input.txt".format(file_name), "r")
output_file = open("Test Cases/{}_output.txt".format(file_name), "w")

input = input_file.read().splitlines()
T = int(input.pop(0))

for t in range(T):
    N = int(input.pop(0))

    # get rows and replace '.'s with Cij
    rows = []
    for n in range(N):
        row = list(input.pop(0))
        for index in range(N):
            if row[index] == '.':
                row[index] = 'C{}{}'.format(n, index)
        rows.append(row)

    # transpost rows to columns
    columns = list(map(list, zip(*rows)))

    # filter out rows and columns that have 'O's
    rows = [row for row in rows if 'O' not in row]
    columns = [column for column in columns if 'O' not in column]

    # get number of 'X's to win
    win_cases = [list(c) for c in set(tuple(c) for c in rows + columns)]
    count_Xs = [N - c.count('X') for c in win_cases]

    # get min number of 'X's to win
    if len(count_Xs) == 0:
        output = "Case #{}: Impossible".format(t + 1)
    else:
        min_Xs = min(count_Xs)
        count_min_Xs = count_Xs.count(min_Xs)
        output = "Case #{}: {} {}".format(t + 1, min_Xs, count_min_Xs)

    output_file.write("{}\n".format(output))
    print(output)

input_file.close()
output_file.close()
