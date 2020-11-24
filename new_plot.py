import sys
import csv
import geopy
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
from optparse import OptionParser

GEO_COLNUM = 5
DATE_COLNUM = 1

csv.register_dialect('managequotes', escapechar='\\', doublequote=False)

def location2coords(locationstr, geolocator):
    try:
        loc = geolocator.geocode(locationstr)
        coords = (loc.longitude, loc.latitude)
        return coords
    except AttributeError as ae:
        print("Attribute error: {} \n At line {} \n Skipping this line and continuing.\n".format(ae, locationstr))

def formatdate(datetimestr):
    # simply chops time from datetime string in CSV and returns only date in y-m-d format
    return datetimestr.split(" ")[0]

def tweets_csv2df(filename, outfilename):
    '''
    Extracts from tweet CSV the (tweet geocode, date) tuples.

    Args:
        filename: str filename of tweets CSV. 
    Returns: 
        df with tweet-geocode and date columns
    '''
    with open(filename) as fin:
        tweet_data = csv.reader(fin, delimiter=';', dialect=csv.get_dialect('managequotes'))
        geolocator = Nominatim(user_agent="my_scraper_application")
        geodate_tuples = list()
        for line in tweet_data:
            if line[GEO_COLNUM] != "":
                coords = location2coords(line[GEO_COLNUM], geolocator)
                datestr = formatdate(line[DATE_COLNUM])
                if coords is not None and len(datestr) == 10:
                    geodate_tuples.append([coords[0], coords[1], datestr])
        print("done geolocating")
        df = pd.DataFrame(geodate_tuples, columns=['lon', 'lat', 'date'])
        print(df.head())
        df.to_csv(outfilename, index=False)
        return df

def makeplot(df, imgname):
    fig = px.density_mapbox(df, lat='lat', lon='lon', radius = 5, mapbox_style='stamen-terrain', center={'lat':39.8283, 'lon':-98.5795}, zoom=2.5)
    fig.write_image("./images/{}.png".format(imgname))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        outfilename = sys.argv[2] 
        df = tweets_csv2df(filename, outfilename)
    else:
        imagename = sys.argv[1]
        df = pd.read_csv("out1.csv")
        makeplot(df, imagename)


