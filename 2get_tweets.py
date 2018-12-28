#within this doc
import csv
import geopy
from geopy.geocoders import Nominatim

GEOCOL = 5
DATECOL = 2

def geo_pull():
    """Returns a set of tweet locations from the csv file of #blacklivesmatter
    tweets"""
    with open('output_got.csv', 'r') as fin:
        tweet_data = list(csv.reader(fin, delimiter=';'))
        geo_set = {(row[GEOCOL],row[DATECOL]) for row in tweet_data[1:] if len(row[GEOCOL])<50 and len(row[GEOCOL])>1}
        #added row[DATECOL]^^
    #for geo in geo_set:
    #    print(str(geo))
    return geo_set
    #set of locations

def get_coords(location_set):
    """Uses geopy to pull coordinates from the geo_set, passes over errors from
    set items that arent coordinates, returns set of long/lat tuples."""
    from geopy.geocoders import Nominatim
    #coord_list = list()
    #print(str(location_set)+"!")

    with open('tweet_coords.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(['Longitude','Latitude','Date'])
        for line in location_set:
            #print("___" + str(geotag))
            y = str(line[1][1])[0:4]
            m = str(line[1][1])[5:7]
            d = str(line[1][1])[8:10]
            if m[0] = 0:
                m = m[1]
            if d[0] = 0:
                d = d[1]
            geolocator = Nominatim()
            location = geolocator.geocode(line[0])
            #line[0] because line contains (x,y),date
            try:
                writer.writerow([location.longitude,location.latitude,str(y+','+m+','+d)))
                #coord_tuple = (float(location.longitude),float(location.latitude))
                #print(str(coord_tuple))
                #coord_list.append(coord_tuple)
            except AttributeError as ae:
                #print("Caught an attribute error: {} -- moving on.".format(ae))
                #print(str(geotag))
                continue



#now have list of coordinates to plot, need to plot onto a map

if __name__ == '__main__':
    #get_coords(geo_pull())
    geo_pull()
