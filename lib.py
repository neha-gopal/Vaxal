import geopandas
import geopy
import os
from fuzzywuzzy import process


#TODO change this to a better api
def to_coords(address):
    locator = geopy.geocoders.Nominatim(user_agent="geolocator")
    location = locator.geocode(address)
    if (location):
        return location
    else :
        return 0



#find nearest address in the file
def nearest_name(filename, name):
    current = [" "]
    currentMax = " "
    currentMaxRatio = 0
    with open(filename) as infile:
        for line in infile:
            current[1] = line
            if processes.extract(name, current)[1] > currentMaxRatio:
                currentMaxRatio = processes.extract(currentMax, current)
                currentMax = current[1]
    return currentMax
