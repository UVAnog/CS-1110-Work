# Nph2tx
# Nolan Harris


import robot


def square():

    r = robot.Robot(1)
    r.say("Ready!")
    n = 0

    while r.check_east():
        r.east()
        n += 1

    else:
        x = (n + 1) ** 2
        r.say(x)


def rectangle():

    r = robot.Robot(2)
    r.say("Ready!")
    s1 = 0
    s2 = 0

    while r.check_east():
        r.east()
        s1 += 1

    else:
        while r.check_south():
            r.south()
            s2 += 1

        else:
            x = (s1 + 1) * (s2 + 1)
            r.say(x)


def middle():

    r = robot.Robot(3)
    r.say("Ready!")
    s1 = 0
    s2 = 0

    while r.check_north():
        r.north()
    while r.check_west():
        r.west()
    while r.check_east():
        r.east()
        s1 += 1
    while r.check_south():
        r.south()
        s2 += 1
    else:
        x = (s1 + 1) * (s2 + 1)
        r.say(x)

def rand():

    r = robot.Robot(4)
    r.say("Ready!")

rand()

