import json, turtle

points = {}

with open("points_mercator.geojson") as f:
    data = json.load(f)

i = 1
for feature in data['features']:
    xy = feature['geometry']['coordinates']
    points[i] = [xy[0],xy[1]]
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
    i+=1
print(len(points))
delka = max_x - min_x
vyska = max_y - min_y

square = [min_x,min_y,delka,vyska]
pseudocode = {}
code = []
#print(square)

def buildQuadtree(array,square,quad,deph):
    if len(array)<=50:#build a leaf node , store P in it, and return node
        print(square,quad,deph,len(array))
        pseudocode[deph] = quad
        if len(array) != 0:
            print(array)
            code = []
            for k in range(deph+1):
                code.append([k,pseudocode[k]])
            print(code)
        return
    else:
        # partition S into 4 quadrants S1, S2, S3, S4 and use them to partition P into P1, P2, P3, P4
        # create a node
        node = [square[0]+square[2]/2,square[1]+square[3]/2]
        S1 = [node[0],node[1],square[2]/2,square[3]/2]
        S2 = [node[0],node[1]-square[3]/2,square[2]/2,square[3]/2]
        S3 = [node[0]-square[2]/2,node[1]-square[3]/2,square[2]/2,square[3]/2]
        S4 = [node[0]-square[2]/2,node[1],square[2]/2,square[3]/2]
        P1 = select_points(array,[node[0],node[0]+square[2],node[1],node[1]+square[3]])
        P2 = select_points(array,[node[0],node[0]+square[2],node[1]-square[3],node[1]])
        P3 = select_points(array,[node[0]-square[2],node[0],node[1]-square[3],node[1]])
        P4 = select_points(array,[node[0]-square[2],node[0],node[1],node[1]+square[3]])
        print(square,quad,deph,len(array))
        pseudocode[deph]=quad
        buildQuadtree(P1, S1,1,deph+1)
        buildQuadtree(P2, S2,2,deph+1)
        buildQuadtree(P3, S3,3,deph+1)
        buildQuadtree(P4, S4,4,deph+1)


def select_points(points,boundaries):
    i = 0
    P = {}
    for k in points:
        point = points[k]
        x = point[0]
        y = point[1]
        if boundaries[0] < x < boundaries[1] and boundaries[2] < y < boundaries[3]:
            i +=1
            P[k] = [point[0],point[1]]
        else:
            continue

    return P

buildQuadtree(points,square,0,0)
