# Library of Functions needed to make the program work
import folium
import pandas as pd
import math
import geocoder

m = folium.Map(location=[6.905319148115447, 79.86877156795114], zoom_start=12)
longitude = 0.0
latitude = 0.0


# get longitude latitude from user

def inputs():
    global longitude
    global latitude
    global closeness

    g = geocoder.ip('me')
    if g.ok:
        parsed_json = g.geojson
        latitude = parsed_json['features'][0]['properties']['lat']
        longitude = parsed_json['features'][0]['properties']['lng']
        closeness = float(2000)
    else:
        print("Error: Unable to retrieve data")


# make the map on the place entered by user
def makeMap():
    m = folium.Map(location=[latitude, longitude], zoom_start=12)


def deg2rad(number):
    pi = math.pi
    rad = number * (pi / 180)
    return rad


def distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the earth in km
    dLat = deg2rad(lat2 - lat1)  # deg2rad below
    dLon = deg2rad(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # Distance in km
    return d


def add_user():
    folium.Marker([latitude, longitude],
                  popup="User",
                  tooltip="User",
                  icon=folium.Icon(icon="heart", icon_color="red")).add_to(m)
    m.save('templates/map.html')


def add_CSV_values_to_map():
    """Get location from csv file and add in to map"""
    global m
    pharms = pd.read_csv('places.csv', index_col=0)
    for index, row in pharms.iterrows():
        phaLatitude = row.loc['Latitude']
        phaLongitude = row.loc['Longitude']
        pharmD = distance(phaLatitude, phaLongitude, latitude, longitude)
        if (pharmD < closeness):
            folium.Marker([phaLatitude, phaLongitude],
                          popup=f"{row.loc['popup']}\n Distance from user : {pharmD:.2f}km",
                          tooltip=f"{row.loc['tooltip']}\n Distance from user : {pharmD:.2f}km",
                          icon=folium.Icon(icon=row.loc['icon type'], icon_color=row.loc['icon color'])).add_to(m)
        m.save('templates/map.html')


def draw_circle_around_user():
    folium.Circle(
        location=[latitude, longitude],
        radius=closeness,
        popup='Love the Area',
        color='blue',
        fill=True,
        fill_color='blue').add_to(m)
    m.save('templates/map.html')
