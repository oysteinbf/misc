import regex as re

with open("data/day20.txt") as f:
    data = f.read().split('\n\n')

def init_tiles(data):
    tiles = {}
    for d in data:
        tile_title = re.findall(r'\d+', d.split('\n')[0])[0]
        tile_data = d.split('\n')[1:]
        E = ''
        W = ''
        for t in tile_data:
            W += t[0]
            E += t[-1]
        N = tile_data[0]
        S = tile_data[-1]
        tiles[tile_title] = [N, E, S, W]
    return tiles


def flip_tile(tile, side):
    if side == 0 or side == 2:  # N or S
        return [tile[0][::-1], tile[3], tile[2][::-1], tile[1]]
    elif side == 1 or side == 3:  # E or W
        return [tile[2], tile[1][::-1], tile[0], tile[3][::-1]]


def compare_tiles(my_tile, other_tile):
    for i in range(0, 4):
        for j in range(0, 4):
            if my_tile[i] == other_tile[j]:
                return my_tile, other_tile, True
            elif my_tile[i][::-1] == other_tile[j]:
                return flip_tile(my_tile, i), other_tile, True
            elif my_tile[i] == other_tile[j][::-1]:
                return my_tile, flip_tile(other_tile, j), True
            elif my_tile[i][::-1] == other_tile[j][::-1]:
                return flip_tile(my_tile, i), flip_tile(other_tile, j), True
            else:
                continue
    return my_tile, other_tile, False

tiles = init_tiles(data)
connections = []
n_connections = {}
for k in tiles.keys():
    n_connections[k] = 0

for my_key in tiles.keys():
    my_tile = tiles[my_key]
    for k in tiles.keys():
        if k == my_key:
            continue
        other_tile = tiles[k]
        tiles[my_key], tiles[k], match = compare_tiles(my_tile, other_tile)
        if match:
            connections.append(my_key+'-'+k)
            n_connections[my_key] += 1

product = 1
for k in n_connections:
    if n_connections[k] == 2:  # i.e. a corner of the image
        product = product * int(k)
print("Part 1: ", product)
