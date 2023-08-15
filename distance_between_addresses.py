import geopy
from geopy import distance
import pandas as pd
import requests
from dotenv import load_env

# Read in addresses

list_1 = pd.read_csv('list_1.csv')
list_2 = pd.read_csv('list_2.csv')

# Find distance from addresses to the lat/long below

to_lat = 39.7148995
to_long = -104.7949419

# First, go through latitude and longitude of dataframe
# Second, use geopy to find the distance between the initial lat/long in the df and the final destination lat/long
# Third, use Google's Distance Matrix API to find the drive time between the two lat/long points (initial / final)
# Google Distance Matrix API - https://developers.google.com/maps/documentation/distance-matrix/distance-matrix

list_1_dist = []
list_1_drive_time =[]
for lat,long in zip(list_1['Latitude'], list_1['Longitude']): 
    list_1_dist.append(distance.distance((lat,long),(to_lat,to_long)).miles)
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={lat}%2C{long}&destinations={to_lat}%2C{to_long}&key={API_KEY}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    drive_time_by_car = response_json['rows'][0]['elements'][0]['duration']['text']
    list_1_drive_time.append(drive_time_by_car)

list_1['distance_to_office'] = list_1_dist
list_1['distance_to_office'] = list_1['distance_to_office'].round(2)
list_1['drive_time'] = list_1_drive_time
list_1.to_csv('list_1.csv')

list_2_dist = []
list_2_drive_time = []
for lat,long in zip(list_2['Latitude'], list_2['Longitude']): 
    list_2_dist.append(distance.distance((lat,long),(to_lat,to_long)).miles)
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={lat}%2C{long}&destinations={to_lat}%2C{to_long}&key={API_KEY}"
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    drive_time_by_car = response_json['rows'][0]['elements'][0]['duration']['text']
    list_2_drive_time.append(drive_time_by_car)

list_2['distance_to_office'] = list_2_dist
list_2['distance_to_office'] = list_2['distance_to_office'].round(2)
list_2['drive_time'] = list_2_drive_time
list_1.to_csv('list_2.csv')