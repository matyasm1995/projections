import json, sys, click

if len(sys.argv) < 4:
    print('too few arguments')
    exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]
group_size = sys.argv[3]


def buildQuadtree(array, square, quad, depth):
    if len(array) <= group_size:
        pseudocode[depth] = str(quad)
        if len(array) != 0:
            for k in range(depth + 1):
                if k == 0:
                    code = pseudocode[k]
                else:
                    code = code + pseudocode[k]
            for i in array:
                out[i] = int(code)
        return
    else:
        node = [square[0] + square[2] / 2, square[1] + square[3] / 2]
        S1 = [node[0], node[1], square[2] / 2, square[3] / 2]
        S2 = [node[0], node[1] - square[3] / 2, square[2] / 2, square[3] / 2]
        S3 = [node[0] - square[2] / 2, node[1] - square[3] / 2, square[2] / 2, square[3] / 2]
        S4 = [node[0] - square[2] / 2, node[1], square[2] / 2, square[3] / 2]
        P1 = select_points(array, [node[0], node[0] + square[2], node[1], node[1] + square[3]])
        P2 = select_points(array, [node[0], node[0] + square[2], node[1] - square[3], node[1]])
        P3 = select_points(array, [node[0] - square[2], node[0], node[1] - square[3], node[1]])
        P4 = select_points(array, [node[0] - square[2], node[0], node[1], node[1] + square[3]])
        pseudocode[depth] = str(quad)
        buildQuadtree(P1, S1, 1, depth + 1)
        buildQuadtree(P2, S2, 2, depth + 1)
        buildQuadtree(P3, S3, 3, depth + 1)
        buildQuadtree(P4, S4, 4, depth + 1)
    return out


def select_points(points, boundaries):
    P = {}
    for k in points:
        point = points[k]
        x = point[0]
        y = point[1]
        if boundaries[0] < x < boundaries[1] and boundaries[2] < y < boundaries[3]:
            P[k] = [point[0], point[1]]
        else:
            continue
    return P


with open(in_file, 'r') as in_f:
    data = json.load(in_f)

points = {}
i = 1
for feature in data['features']:
    xy = feature['geometry']['coordinates']
    points[i] = [xy[0], xy[1]]
    if i == 1:
        min_x = xy[0]
        max_x = xy[0]
        min_y = xy[1]
        max_y = xy[1]
    else:
        if xy[0] < min_x:
            min_x = xy[0]
        if xy[0] > max_x:
            max_x = xy[0]
        if xy[1] < min_y:
            min_y = xy[1]
        if xy[1] > max_y:
            max_y = xy[1]
    i += 1

length = max_x - min_x
height = max_y - min_y

bbox = [min_x, min_y, length, height]
pseudocode = {}
out = {}

x = buildQuadtree(points, bbox, 0, 0)

sorted_by_key = sorted(x.items(), key=lambda kv: kv[0])

i = 0
for feat in data['features']:
    feat['properties']['code'] = sorted_by_key[i][1]
    i += 1

with open(out_file, 'w') as out:
    json.dump(data, out)
