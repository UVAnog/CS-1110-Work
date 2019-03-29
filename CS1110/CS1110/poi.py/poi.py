# Nph2tx
# Nolan Harris
# Katie Sabo
# kbs5fp
import math
import webbrowser

user_lat = float(input('enter latitude: '))
user_lon = float(input('enter longitude: '))


# DO NOT MODIFY the following function; use as is
def distance_between(lat_1, lon_1, lat_2, lon_2):
    '''Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them'''
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06   # 69.09 = circumference of earth in miles / 360 degrees
    return dist

def finder():
    file = open('arbys.csv')
    shortest_distance = 3000
    for line in file:
        text = line.strip().split(',')
        poi_lat = float(text[0])
        poi_lon = float(text[1])
        distance = distance_between(user_lat, user_lon, poi_lat, poi_lon)
        address = (text[4] + text[5] + text[6])
        address.replace(' ', '+')
        url = 'http://maps.google.com/maps?q=' + address
        webbrowser.open(url)
        return distance


finder()
map()
