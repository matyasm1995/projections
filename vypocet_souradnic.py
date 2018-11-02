from math import sin, tan, radians, log
from turtle import forward, right, exitonclick, speed, setpos, down, up, dot, write, ht


def lambert_x(i):
    """
    funkce pro výpočet x-souřadnice Lamberta
    :param i: zeměpisná délka
    :return hodnotu zeměpisné délky v daném souřadnicovém systému:
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def lambert_y(i):
    """
    funkce pro výpočet y-souřadnice Lamberta
    :param i: zeměpisná šířka
    :return hodnotu zeměpisné šířky v daném souřadnicovém systému:
    """
    y = R * sin(radians(i))
    y = round(y, 1)
    return y


def marin_x(i):
    """
    funkce pro výpočet x-souřadnice Marina
    :param i: zeměpisná délka
    :return hodnotu zeměpisné délky v daném souřadnicovém systému:
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def marin_y(i):
    """
    funkce pro výpočet y-souřadnice Marina
    :param i: zeměpisná šířka
    :return hodnotu zeměpisné šířky v daném souřadnicovém systému:
    """
    y = R * (radians(i))
    y = round(y, 1)
    return y


def braun_x(i):
    """
    funkce pro výpočet x-souřadnice Brauna
    :param i: zeměpisná délka
    :return hodnotu zeměpisné délky v daném souřadnicovém systému:
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def braun_y(i):
    """
    funkce pro výpočet y-souřadnice Brauna
    :param i: zeměpisná šířka
    :return hodnotu zeměpisné šířky v daném souřadnicovém systému:
    """
    y = 2 * R * tan((radians(i)) / 2)
    y = round(y, 1)
    return y


def mercator_x(i):
    """
    funkce pro výpočet x-souřadnice Mercatora
    :param i: zeměpisná délka
    :return hodnotu zeměpisné délky v daném souřadnicovém systému:
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def mercator_y(i):
    """
    funkce pro výpočet y-souřadnice Brauna
    :param i: zeměpisná šířka
    :return hodnotu zeměpisné šířky v daném souřadnicovém systému:
    """
    y = R * log((1 / tan(((radians(90 - i)) / 2))))
    y = round(y, 1)
    return y


def longitude(projection_x):
    """
    funkce, která vytváří a tiskne pole x-souřadnic v určených zeměpisných délkách pro dané zobrazení
    :param projection_x: zobrazení
    """
    for i in range(-180, 181, 10):
        x = (projection_x(i))
        if x > 100 or x < -100: #osetreni prilis velkeho x
            lons.append('-')
        else:
            lons.append(x)
    print('meridians: ' + str(lons))
    return lons


def latitude(projection_y):
    """
    funkce, která vytváří a tiskne pole y-souřadnic v určených zeměpisných šířkách pro dané zobrazení
    :param projection_y: zobrazení
    """
    for i in range(-90, 91, 10):
        try:
            y = (projection_y(i))
            if y > 100 or y < -100: #osetreni prilis velkeho y
                lats.append('-')
            else:
                lats.append(y)
        except: #osetreni mercatora
            lats.append("-")
    print('parallels: ' + str(lats))
    return lats


def inputFloat(message):
    """
    funkce na ověření, že vstup je float
    :param message: uživatelův vstup
    """
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Not a number")
            continue
        return userInput


def inputInteger(message):
    """
    funkce na ověření, že vstup je celé číslo
    :param message: uživatelův vstup
    """
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not a integer")
            continue
        return userInput


def point_calc(projection_x, projection_y):
    """
    funkce pro výpočet mapových souřadnic zadaného bodu
    :param projection_x: funkce pro výpočet zobrazení
    :param projection_y: funkce pro výpočet zobrazení
    :return: pole zadaných bodů
    """
    while point != [0, 0]:
        p = []
        point[0] = inputFloat('enter longitude of point: ')
        while point[0] > 180 or point[0] < -180: #osetreni spravneho rozsahu zem. sirky
            point[0] = inputFloat('enter longitude of point again: ')
        point[1] = inputFloat('enter latitude of point: ')
        while point[1] > 90 or point[1] < -90: #osetreni spravneho rozsahu zem. delky
            point[1] = inputFloat('enter latitude of point again: ')
        if -100 < projection_x(point[0]) < 100: #osetreni prilis velkeho x
            x = projection_x(point[0])
            p.append(x)
            print('x = ' + str(x))

        else:
            print('x = - ')
        try:
            if -100 < projection_y(point[1]) < 100: #osetreni prilis velkeho y
                y = projection_y(point[1])
                print('y = ' + str(y))
                p.append(y)
            else:
                print('y = -')
        except:
            print('y = -')
        if len(p) == 2:
            if type(p[0]) == float and type(p[1]) == float:
                point_g.append(p)
    return point_g

def graphic(lats, lons, point_g):
    """
    funkce pro vykresleni souradnicove site
    :param i: index prvku pole y-souřadnic
    :param j: index prvku pole x-souřadnic
    :param lats: pole souřadnic zeměpisné šířky
    :param lons: pole souřadnic zeměpisné délky
    :param point_g: pole bodů pro vykreslení
    :return: kreslí grafiku
    """
    speed(10)
    ht()
    m = int((len(lons) + 1) / 2)  # vypocet poctu rovnobezek
    n = int((len(lats) + 1) / 2 - 1)  # vypocet poctu rovnobezek
    while m < (len(lons)): #spocitani delky poloviny rovniku
        try:
            x = float(lons[m])
            m = m + 1
        except:
            break
    while n < (len(lats)): #vykresleni rovnobezek
        try:
            y = float(lats[n])
            up()
            setpos(x * -10, y * 10)
            down()
            forward(2 * x * 10)
            up()
            setpos(x * -10, -y * 10)
            down()
            forward(2 * x * 10)
            up()
            n = n + 1
        except:
            break
    xm = x / ((m - 1) / 2)
    right(90)
    for m in range(m): #vykresleni poledniku
        setpos(-10 * x, y * 10)
        down()
        forward(20 * y)
        up()
        x = x - xm
    for k in range(len(point_g)-1):
        up()
        setpos((point_g[k][0])*10, (point_g[k][1])*10)
        down()
        dot(5, "red")
        write((k+1), False, align="right")
    exitonclick()


lats = []
lons = []
point = [1, 1]
point_g = []

projection = input('set projection: ')  # zjisteni zobrazeni
while projection not in ('L', 'A', 'B', 'M' ):
    print('choose L for Lambert, A for Marin, B for Braun or M for Mercator: ')
    projection = input('set projection: ')

radius = inputFloat('set the radius of the Earth in km or enter 0 to set radius to 6371.11km: ') #zjisteni polomeru Zeme
while radius < 0:
    radius = inputFloat('set the radius of the Earth in km or enter 0 to set radius to 6371.11km: ')
if radius == 0:
    radius = 6371.11

scale = inputInteger('set the scale: ') #zjisteni meritka
while scale <= 0:
    scale = inputInteger('set the scale again: ')

R = abs((radius / scale) * 100000)  # uprava polomeru Zeme meritkem

if projection == 'L':  # vypsani hodnot z.s. a z.d. pro lamberta + vypocet souradnic bodu
    longitude(lambert_x)
    latitude(lambert_y)
    point_calc(lambert_x, lambert_y)

if projection == 'A':  # vypsani hodnot z.s. a z.d. pro marina + vypocet souradnic bodu
    longitude(marin_x)
    latitude(marin_y)
    point_calc(marin_x, marin_y)

if projection == 'B':  # vypsani hodnot z.s. a z.d. pro brauna + vypocet souradnic bodu
    longitude(braun_x)
    latitude(braun_y)
    point_calc(braun_x, braun_y)

if projection == 'M':  # vypsani hodnot z.s. a z.d. pro mercatora + vypocet souradnic bodu
    longitude(mercator_x)
    latitude(mercator_y)
    point_calc(mercator_x, mercator_y)

try:
    graphic(lats, lons, point_g) #grafika
except:
    print("too large scale to draw grid")
