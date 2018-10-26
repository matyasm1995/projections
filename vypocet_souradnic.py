from math import sin, tan, radians, log
from turtle import forward, left, right, exitonclick, speed


def lambert_x(i):  # vypocet lamberta
    x = R * (radians(i))
    x = round(x, 1)
    return x


def lambert_y(i):
    y = R * sin(radians(i))
    y = round(y, 1)
    return y


def marin_x(i):  # vypocet marina
    x = R * (radians(i))
    x = round(x, 1)
    return x


def marin_y(i):
    y = R * (radians(i))
    y = round(y, 1)
    return y


def braun_x(i):  # vypocet brauna
    x = R * (radians(i))
    x = round(x, 1)
    return x


def braun_y(i):
    y = 2 * R * tan((radians(i)) / 2)
    y = round(y, 1)
    return y


def mercator_x(i):  # vypocet mercatora
    x = R * (radians(i))
    x = round(x, 1)
    return x


def mercator_y(i):
    y = R * log((1 / tan(((radians(90 - i)) / 2))))
    y = round(y, 1)
    return y


def delka(zobrazeni_x):
    for i in range(-180, 181, 10):
        x = (zobrazeni_x(i))
        if x > 100 or x < -100:
            long.append('-')
        else:
            long.append(x)
    print('meridians: ' + str(long))


def sirka(zobrazeni_y):
    for i in range(-90, 91, 10):
        try:
            y = (zobrazeni_y(i))
            if y > 100 or y < -100:
                lat.append('-')
            else:
                lat.append(y)
        except:
            lat.append("-")
    print('parallels: ' + str(lat))


def inputNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not a number")
            continue
        else:
            return userInput


def bod(zobrazeni_x, zobrazeni_y):
    while point != [0, 0]:
        point[0] = inputNumber('enter latitude of point')
        while point[0] > 90 or point[0] < -90:
            point[0] = inputNumber('enter latitude of point again')
        point[1] = inputNumber('enter longitude of point')
        while point[1] > 180 or point[1] < -180:
            point[1] = inputNumber('enter longitude of point again')
        try:  # osetreni mercatora
            if -100 < zobrazeni_y(point[0]) < 100:
                print('x = ' + str(zobrazeni_y(point[0])))
            else:
                print('x = - ')
        except:
            print('x = -')
        if -100 < zobrazeni_x(point[1]) < 100:
            print('y = ' + str(zobrazeni_x(point[1])))
        else:
            print('y = -')


lat = []
long = []
point = [1, 1]

projection = input('set projection')  # zjisteni zobrazeni
while projection != "L" and projection != 'A' and projection != 'B' and projection != 'M':
    print('choose L for Lambert, A for Marin, B for Braun or M for Mercator')
    projection = input('set projection')

radius = inputNumber('set the radius of the Earth in km or enter 0 to set radius to 6371.11km')
while radius < 0:
    radius = inputNumber('set the radius of the Earth in km or enter 0 to set radius to 6371.11km')
if radius == 0:
    radius = 6371.11

scale = inputNumber('set the scale')
while scale <= 0:
    scale = inputNumber('set the scale again')

R = abs((radius / scale) * 100000)  # uprava polomeru Zeme meritkem

if projection == 'L':  # vypsani hodnot z.s. a z.d. pro lamberta + vypocet souradnic bodu
    delka(lambert_x)
    sirka(lambert_y)
    bod(lambert_x, lambert_y)

if projection == 'A':  # vypsani hodnot z.s. a z.d. pro marina + vypocet souradnic bodu
    delka(marin_x)
    sirka(marin_y)
    bod(marin_x, marin_y)

if projection == 'B':  # vypsani hodnot z.s. a z.d. pro brauna + vypocet souradnic bodu
    delka(braun_x)
    sirka(braun_y)
    bod(braun_x, braun_y)

if projection == 'M':  # vypsani hodnot z.s. a z.d. pro mercatora + vypocet souradnic bodu
    delka(mercator_x)
    sirka(mercator_y)
    bod(mercator_x, mercator_y)

for k in range(0, 8, 2):
    forward((long[36]) * 10)
    left(90)
    forward((lat[(10 + k)] - lat[10 + k - 1]) * 10)
    left(90)
    forward((long[36]) * 10)
    right(90)
    forward((lat[(10 + k + 1)] - lat[10 + k]) * 10)
    right(90)

forward((long[36]) * 10)
left(90)
forward((lat[(18)] - lat[17]) * 10)
left(90)
forward((long[36]) * 10)
left(90)

for i in range(9):
    forward(lat[18] * 10)
    left(90)
    forward(long[19] * 10)
    left(90)
    forward(lat[18] * 10)
    right(90)
    forward(long[19] * 10)
    right(90)

exitonclick()
