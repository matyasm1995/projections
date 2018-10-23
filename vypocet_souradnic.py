from math import sin, tan, radians, log
from turtle import forward, left, right, exitonclick, speed


p = input('set projection')
while p != "L" and p != 'A' and p != 'B' and p != 'M':
    print('choose L for Lambert, A for Marin, B for Braun or M for Mercator')
    p = input('set projection')

try:
    r = float(input('set the radius of the Earth in km or enter 0 to set radius to 6371.11km'))
except ValueError:
    print('you did not enter a number')
    r = float(input('set the radius of the Earth in km again or enter 0 to set radius to 6371.11km'))

if r == 0:
    r = 6371.11
try:
    m = int(input('set the scale'))
except ValueError:
    print('scale has to be integer')
    m = int(input('set the scale again'))

R = abs((r / m) * 100000)

lat = []
long = []
point = [1,1]

def lambert_x(lam):
    x = R * (radians(lam))
    xr = round(x, 1)
    if xr>100 or xr<-100:
        return ('-')
    else:
        return xr

def lambert_y(fi):
    y = R * sin(radians(fi))
    yr = round(y, 1)
    if yr>100 or yr<-100:
        return ('-')
    else:
        return yr

def marin_x(lam):
    x = R * (radians(lam))
    xr = round(x, 1)
    if xr>100 or xr<-100:
        return ('-')
    else:
        return xr

def marin_y(fi):
    y = R * (radians(fi))
    yr = round(y, 1)
    if yr>100 or yr<-100:
        return ('-')
    else:
        return yr

def braun_x(lam):
    x = R * (radians(lam))
    xr = round(x, 1)
    if xr>100 or xr<-100:
        return ('-')
    else:
        return xr

def braun_y(fi):
    y = 2 * R * tan((radians(fi)) / 2)
    yr = round(y, 1)
    if yr>100 or yr<-100:
        return ('-')
    else:
        return yr

def mercator_x(lam):
    x = R * (radians(lam))
    xr = round(x, 1)
    if xr>100 or xr<-100:
        return ('-')
    else:
        return xr

def mercator_y(fi):
    y = R * log((1 / tan(((radians(90 - fi)) / 2))))
    yr = round(y, 1)
    if yr>100 or yr<-100:
        return ('-')
    else:
        return yr

if p == 'L':
    for lam in range(-180,181,10):
        long.append(lambert_x(lam))
    for fi in range(-90,91,10):
        lat.append(lambert_y(fi))
    print('parallels: ' + str(lat))
    print('meridians: ' + str(long))
    while point != [0,0]:
        point[0] = (float(input('enter latitude of point')))
        point[1] = (float(input('enter longitude of point')))
        print('x = ' + str(lambert_x(point[0])))
        print('y = ' + str(lambert_y(point[1])))

if p == 'A':
    for lam in range(-180,181,10):
        long.append(marin_x(lam))
    for fi in range(-90,91,10):
        lat.append(marin_y(fi))
    print('parallels: ' + str(lat))
    print('meridians: ' + str(long))
    while point != [0,0]:
        point[0] = (float(input('enter latitude of point')))
        point[1] = (float(input('enter longitude of point')))
        print('x = ' + str(marin_x(point[0])))
        print('y = ' + str(marin_y(point[1])))

if p == 'B':
    for lam in range(-180,181,10):
        long.append(braun_x(lam))
    for fi in range(-90,91,10):
        lat.append(braun_y(fi))
    print('parallels: ' + str(lat))
    print('meridians: ' + str(long))
    while point != [0,0]:
        point[0] = (float(input('enter latitude of point')))
        point[1] = (float(input('enter longitude of point')))
        print('x = ' + str(braun_x(point[0])))
        print('y = ' + str(braun_y(point[1])))

if p == 'M':
    for lam in range(-180,181,10):
        long.append(mercator_x(lam))
    for fi in range(-90,91,10):
        try:
            lat.append(mercator_y(fi))
        except ZeroDivisionError:
            lat.append('-')
            continue
    print('parallels: ' + str(lat))
    print('meridians: ' + str(long))
    while point != [0,0]:
        point[0] = (float(input('enter latitude of point')))
        point[1] = (float(input('enter longitude of point')))
        print('x = ' + str(mercator_x(point[0])))
        print('y = ' + str(mercator_y(point[1])))


for k in range(int(len(lat)/2)):
    for i in range(len(long)):
        forward((long[i]-long[i-1])*10)
    left(90)
    forward((lat[int(len(lat)/2+k+1)])*10)
    left(90)
    for i in range(len(long)):
        forward((long[i]-long[i-1])*10)
        left(0)
    right(90)
    forward((lat[int(len(lat) / 2 + k+1)])*10)
    right(90)
exitonclick()

'''for i in range(4):
    forward((long[36])*10)
    left(90)
    forward((lat[10]) * 10)
    left(90)
    forward((long[36]) * 10)
    right(90)
    forward((lat[10]) * 10)
    right(90)

forward((long[36])*10)
left(90)
forward((lat[10]) * 10)
left(90)
forward((long[36]) * 10)
left(90)

for i in range(9):
    forward((lat[18])*10)
    left(90)
    forward((long[19]) * 10)
    left(90)
    forward((lat[18]) * 10)
    right(90)
    forward((long[19]) * 10)
    right(90)

forward((lat[18])*10)
right(90)
exitonclick()'''




