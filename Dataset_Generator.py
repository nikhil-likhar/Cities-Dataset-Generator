# Main Code
#Obtaining Longitude and lattitude of given cities(in data Dictionary) using Geolocator.geocode and storing in the File "Lat_Long.csv" and pring the dictionary of log and latt of Cities

#Obtaining the Distances of Cities using Geopy and storing in "Distances.csv" and Printing the Dictionary of the same.

import pandas as pd
import folium
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim 
import pandas as pd
import time
import csv
from geopy.distance import geodesic

#Cities

print("\n\n\n****** This Code Generates the dataset for the given number of Cities ******\n")
print("\n****** Dataset generated are :")
print("     1) Lattitude and Lattitude of given cities\n     2) Distances between each city to every city for given cities\n\n")
print("******You can also edit the cities to generate the dataset for\n\n\n")

num=int(input("\n\n\nEnter the number of Cities for which to generate Dataset : "))

if(num<=20):
    cities = ['Bangalore','Hyderabad','Kolkata','Delhi','Bhopal','Thiruvananthapuram','Lucknow','Chennai','Srinagar','Gandhinagar','Mumbai','Ahmedabad','Pune','Nagpur','Jaipur','Chandigarh','Guwahati','Indore','Aurangabad','Patna',
         'Goa','Visakhapatnam','Ranchi','Gandhinagar','Bikaner','S']
else:
    cities= ['Kolapur', 'Ahmedabad', 'Vellore', 'Agra', 'Cuttack', 'Guwahati', 'Kolkata', 'Aligarh', 'Madurai', 'Raipur', 'Thiruvananthapuram', 'Jhansi', 'Patiala', 'Visakhapatnam', 'Kota', 'Jaipur', 'Jammu', 'Goa', 'Chennai', 'Varanasi', 'Vadodara', 'Jamshedpur', 'Aurangabad', 'Jabalpur', 'Leh', 'Gandhinagar', 'Jaisalmer', 'Chandigarh', 'Hyderabad', 'Nashik', 'Ranchi', 'Pune', 'Jodhpur', 'Indore', 'Jalgaon', 'Nanded', 'Gangtok', 'Bhopal', 'Patna', 'Srinagar', 'Delhi', 'Gwalior', 'Solapur', 'Bangalore', 'Bikaner', 'Ghaziabad', 'Rajkot', 'Lucknow', 'Dwarka', 'Mumbai', 'Nagpur']

cities=cities[:num]    
print("\n\n\n\nCurrently Cities are:\n\n",cities)


df = pd.DataFrame() 

#To get the Lattitude and longitude and generate its csv file
longitude = [] 
latitude = [] 
   
points=[]
def findGeocode(city):    
    try:  
        geolocator = Nominatim(user_agent="your_app_name") 
        return geolocator.geocode(city) 
      
    except GeocoderTimedOut: 
        return findGeocode(city)     
  
for i in cities: 
      
    if findGeocode(i) != None: 
           
        loc = findGeocode(i) 
        lat=loc.latitude
        long=loc.longitude
        points.append((lat,)+(long,)) 
        latitude.append(lat)
        longitude.append(long)
       
    else: 
        latitude.append(np.nan) 
        longitude.append(np.nan) 
df["City"]=cities        
df["Latitude"] = latitude 
df["Longitude"] = longitude 
df.to_csv('Lat_Long.csv')         


print("\n\n\n\nLattitude and Longitude of Cities:\n\n",points,"\n\n\n") 







#To find the distances from every city to every other city

dist = {}
for city_index, [c1_lat, c1_long] in enumerate(points):
    temp = []
    for c2_lat, c2_long in points:
        city1 = (c1_lat, c1_long)
        city2 = (c2_lat, c2_long)
        val = round(geodesic( city1, city2).km, 3)
        #logic for appending
        if int(val) == 0:
            temp.append(100000)
        #elif int(val) >= 500:
            #temp.append(100000)
        else:
            temp.append(val)
    dist[ cities[city_index] ] = temp
print("\n\nDistances from each city to every other city\n\n",dist)

dist_df = pd.DataFrame()
dist_df['cities'] = cities
data1 = pd.DataFrame(dist, index=cities)
#print(data1)
data1.to_csv('Distances.csv')


print("\n\n\n\nThe file \"Lat_Long.csv\" is generated with Lattitude and Longitude")
print("\n\n\n\nThe file \"Distances.csv\" is generated with Distances from each city to every other city")
