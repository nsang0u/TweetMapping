import csv
import geopy
from geopy.geocoders import Nominatim

GEOCOL = 5

def geo_pull():
    """Returns a set of tweet locations from the csv file of #blacklivesmatter tweets
    
    currently hardcoded to take output_got.csv as tweet data

    TODO: accept input file as commandline argument

    """
    with open('output_got.csv', 'r') as fin:
        tweet_data = list(csv.reader(fin, delimiter=';'))
        geo_set = {row[GEOCOL] for row in tweet_data[1:] if len(row[GEOCOL])<50 and len(row[GEOCOL])>1}
    return geo_set

def get_coords(location_set):
    """
    Uses geopy to pull coordinates from the geo_set, passes over errors from
    set items that arent coordinates, returns set of long/lat tuples.

    
    Currently writes to tweet_coords.csv

    TODO: create unique time/date filename for each run. 
    """
    from geopy.geocoders import Nominatim
    with open('tweet_coords.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(['Longitude','Latitude'])
        for geotag in location_set:
            geolocator = Nominatim()
            location = geolocator.geocode(geotag)
            try:
                writer.writerow([location.longitude,location.latitude])
            except AttributeError as ae:
                continue

if __name__ == '__main__':
    get_coords(geo_pull())
