# Running: `python gold_mine_chaper_2.py [sample | validation | final]`

import sys

file_name = sys.argv[1]
input_file = open("Test Cases/{}_input.txt".format(file_name), "r")
output_file = open("Test Cases/{}_output.txt".format(file_name), "w")

input = input_file.read().splitlines()
T = int(input.pop(0))

is_has_exit = False


def get_maximum_gold_in_cave(caves, cave_index, starting):
    global is_has_exit

    cave = caves[cave_index]
    tunnels = cave['tunnels']

    if len(cave['tunnels']) == 0:
        return
    if cave_index == 0 and starting:
        is_has_exit = True
        return

    # get the maximum gold in the next caves
    for t in tunnels:
        caves[t]['tunnels'] = [
            tunnel for tunnel in caves[t]['tunnels'] if tunnel != cave_index]
        get_maximum_gold_in_cave(caves, t, True)
        caves[t]['tunnels'] = [
            cave_index] + caves[t]['tunnels']

    # get the best tunnel of the cave
    best_tunnel = max([caves[tunnel]
                       for tunnel in tunnels], key=lambda t: t['gold'])
    cave['gold'] += best_tunnel['gold'] if not best_tunnel['visited'] else 0
    cave['tunnels'] = [
        tunnel for tunnel in tunnels if tunnel != best_tunnel['index']]
    best_tunnel['tunnels'] = [
        tunnel for tunnel in tunnels if tunnel != cave_index]
    best_tunnel['visited'] = True

    # update additional gold
    for t in tunnels:
        if (caves[t]['index'] != best_tunnel['index']):
            cave['additional_gold'] += [caves[t]['gold']]
        cave['additional_gold'] += caves[t]['additional_gold']


for t in range(T):
    N, K = input.pop(0).split(' ')
    N = int(N)
    K = int(K)
    is_has_exit = False

    # create caves
    caves = []
    for index, gold in enumerate(input.pop(0).split(' ')):
        caves.append({
            'index': index,
            'original_gold': int(gold),
            'gold': int(gold),
            'visited': False,
            'tunnels': [],
            'additional_gold': []
        })

    # create tunnels
    for i in range(N - 1):
        c1, c2 = input.pop(0).split(' ')
        caves[int(c1) - 1]['tunnels'].append(int(c2) - 1)
        caves[int(c2) - 1]['tunnels'].append(int(c1) - 1)

    # get the maximum gold in each cave
    get_maximum_gold_in_cave(caves, 0, False)

    if len(caves[0]['additional_gold']) and K > 0:
        first_layer_gold = [caves[tunnel]['gold']
                            for tunnel in caves[0]['tunnels']]
        other_layer_gold = [gold for gold in caves[0]
                            ['additional_gold'] if gold not in first_layer_gold]
        first_layer_gold.sort(reverse=True)
        other_layer_gold.sort(reverse=True)

        # create exit
        if K > 0 and not is_has_exit:
            if len(first_layer_gold):
                caves[0]['gold'] += first_layer_gold[0]
                first_layer_gold.pop(0)
            elif K > 1 and len(other_layer_gold) > 1:
                caves[0]['gold'] += other_layer_gold[0] + other_layer_gold[1]
                other_layer_gold.pop(0)
                other_layer_gold.pop(0)
                K -= 1
            is_has_exit = True
            K -= 1

        # create new tunnels
        while K > 0 and len(first_layer_gold) and len(other_layer_gold):
            caves[0]['gold'] += first_layer_gold[0] + other_layer_gold[0]
            first_layer_gold.pop(0)
            other_layer_gold.pop(0)
            K -= 1
        remain_gold = first_layer_gold + other_layer_gold
        while K > 0 and len(remain_gold):
            caves[0]['gold'] += remain_gold[0]
            remain_gold.pop(0)
            K -= 1

        output = "Case #{}: {}".format(t + 1, caves[0]['gold'])

    elif K > 0:
        output = "Case #{}: {}".format(t + 1, caves[0]['gold'])

    else:
        output = "Case #{}: {}".format(t + 1, caves[0]['original_gold'])

    output_file.write("{}\n".format(output))
    print(output)

input_file.close()
output_file.close()
