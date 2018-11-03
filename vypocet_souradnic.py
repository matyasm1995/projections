from math import sin, tan, radians, log
from turtle import forward, right, exitonclick, speed, setpos, down, up, dot, write, ht


def lambert_x(i):
    """
    function for calculating the map coordinates of the meridians using the Lambert projection
    :param i: longitude
    :return: the value of the longitude in the specified coordinate system
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def lambert_y(i):
    """
    function for calculating the map coordinates of the parallels using the Mercator projection
    :param i: latitude
    :return: the value of the latitude in the specified coordinate system
    """
    y = R * sin(radians(i))
    y = round(y, 1)
    return y


def marin_x(i):
    """
    function for calculating the map coordinates of the meridians using the Marin projection
    :param i: longitude
    :return: the value of the longitude in the specified coordinate system
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def marin_y(i):
    """
    function for calculating the map coordinates of the parallels using the Marin projection
    :param i: latitude
    :return: the value of the latitude in the specified coordinate system
    """
    y = R * (radians(i))
    y = round(y, 1)
    return y


def braun_x(i):
    """
    function for calculating the map coordinates of the meridians using the Braun projection
    :param i: longitude
    :return: the value of the longitude in the specified coordinate system
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def braun_y(i):
    """
    function for calculating the map coordinates of the parallels using the Braun projection
    :param i: latitude
    :return: the value of the latitude in the specified coordinate system
    """
    y = 2 * R * tan((radians(i)) / 2)
    y = round(y, 1)
    return y


def mercator_x(i):
    """
    function for calculating the map coordinates of the meridians using the Mercator projection
    :param i: longitude
    :return: the value of the longitude in the specified coordinate system
    """
    x = R * (radians(i))
    x = round(x, 1)
    return x


def mercator_y(i):
    """
    function for calculating the map coordinates of the parallels using the Mercator projection
    :param i: latitude
    :return: the value of the latitude in the specified coordinate system
    """
    y = R * log((1 / tan(((radians(90 - i)) / 2))))
    y = round(y, 1)
    return y


def longitude(projection_x):
    """
    function that creates and prints the x-coordinate array at certain latitudes for the specified projection
    :param projection_x: function for calculation x-coordinate
    :return: array of map coordinates of meridians

    """
    for i in range(-180, 181, 10):
        x = (projection_x(i))
        if x > 100 or x < -100:  # limits for map coordinates of x
            continue
        else:
            lons.append(x)
    print('meridians: (' + "-; " * int(((37 - len(lons)) / 2)) + "; ".join(map(str, lons)) +
          "; -" * int(((37 - len(lons)) / 2)) + ')')
    return lons


def latitude(projection_y):
    """
    function that creates and prints the y-coordinate array at certain latitudes for the specified projectiontváří a tiskne pole y-souřadnic v určených zeměpisných šířkách pro dané zobrazení
    :param projection_y: function for calculation y-coordinate
    :return: array of map coordinates of parallels
    """
    for i in range(-90, 91, 10):
        try:
            y = (projection_y(i))
            if y > 100 or y < -100:  # limits for map coordinates of x
                continue
            else:
                lats.append(y)
        except:  # handling Mercator
            continue
    print('parallels: (' + "-; " * int(((19 - len(lats)) / 2)) + "; ".join(map(str, lats)) +
          "; -" * int(((19 - len(lats)) / 2)) + ')')
    return lats


def inputFloat(message):
    """
    function to verify that the input is float
    :param message: user input
    :return: user input
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
    function to verify that the input is integer
    :param message: user input
    :return: user input
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
    function to calculate map coordinates of a specified point
    :param projection_x: function for calculation x-coordinate
    :param projection_y: function for calculation y-coordinate
    :return: array of map coordinates of entered points
    """
    while point != [0, 0]:
        p = []
        point[0] = inputFloat('enter longitude of point: ')
        while point[0] > 180 or point[0] < -180:  # the condition of the correct latitude range
            point[0] = inputFloat('enter longitude of point again: ')
        point[1] = inputFloat('enter latitude of point: ')
        while point[1] > 90 or point[1] < -90:  # the condition of the correct longitude range
            point[1] = inputFloat('enter latitude of point again: ')
        if -100 < projection_x(point[0]) < 100:  # limits for map coordinates of x
            x = projection_x(point[0])
            p.append(x)
            print('x = ' + str(x))
        else:
            print('x = - ')
        try:
            if -100 < projection_y(point[1]) < 100:  # limits for map coordinates of x
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
    function for plotting the coordinate grid and the specified point
    :param lats: array of map coordinates of parallels
    :param lons: array of map coordinates of meridians
    :param point_g: array of map coordinates of entered pointsb
    """
    speed(10)
    ht()
    max_x = max(lons)
    max_y = max(lats)
    x_ten = (2 * max_x) / len(lons)

    for i in range(len(lats)):  # plotting of parallels
        y = float(lats[i])
        up()
        setpos(max_x * -10, y * 10)
        down()
        forward(2 * max_x * 10)

    right(90)

    for j in range(len(lons) + 1):  # plotting of meridians
        setpos(-10 * max_x, max_y * 10)
        down()
        forward(20 * max_y)
        up()
        max_x = max_x - x_ten

    for k in range(len(point_g) - 1): # plotting of points
        up()
        setpos((point_g[k][0]) * 10, (point_g[k][1]) * 10)
        down()
        dot(5, "red")
        write((k + 1), False, align="right")
    exitonclick()


lats = []
lons = []
point = [1, 1]
point_g = []

projection = input('set projection: ')  # detection of the projection
while projection not in ('L', 'A', 'B', 'M'):
    print('choose L for Lambert, A for Marin, B for Braun or M for Mercator: ')
    projection = input('set projection: ')

radius = inputFloat(
    'set the radius of the Earth in km or enter 0 to set radius to 6371.11km: ')  # detection of the radius of the Earth
while radius < 0:
    radius = inputFloat('set the radius of the Earth in km or enter 0 to set radius to 6371.11km: ')
if radius == 0:
    radius = 6371.11

scale = inputInteger('set the scale: ')  # detection of the scale of the Earth
while scale <= 0:
    scale = inputInteger('set the scale again: ')

R = (radius / scale) * 100000  # convert the Earth's radius by scale

if projection == 'L':
    longitude(lambert_x)
    latitude(lambert_y)
    point_calc(lambert_x, lambert_y)

if projection == 'A':
    longitude(marin_x)
    latitude(marin_y)
    point_calc(marin_x, marin_y)

if projection == 'B':
    longitude(braun_x)
    latitude(braun_y)
    point_calc(braun_x, braun_y)

if projection == 'M':
    longitude(mercator_x)
    latitude(mercator_y)
    point_calc(mercator_x, mercator_y)

graphic(lats, lons, point_g)
