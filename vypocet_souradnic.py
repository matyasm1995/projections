from math import sin, tan,radians, log

r = 6371.11
m = 50000000
R=(r/m)*100000
def lambert (lam,fi):
    x = R*(radians(lam))
    y = R*sin(radians(fi))
    return(x,y)

print(lambert(-180,-90))

def marin (lam,fi):
    x = R * (radians(lam))
    y = R * (radians(fi))
    return (x,y)

print(marin(-180,-90))

def braun (lam,fi):
    x = R * (radians(lam))
    y = 2*R*tan((radians(fi))/2)
    return (x,y)

print(braun(-180,-90))

def mercator (lam,fi):
    x = R * (radians(lam))
    y = R * log((1 / tan(((radians(90-fi)) / 2))))
    return (x,y)

print(mercator(-180,-85))

