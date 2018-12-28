import sys
import csv
import math
from region import Region
#defining the radius of the point marking each tweet in coordinate.
POINT_RAD = .1

def mercator(lat):
    """project latitude 'lat' according to Mercator"""
    lat_rad = (lat * math.pi) / 180
    projection = math.log(math.tan((math.pi / 4) + (lat_rad / 2)))
    return (180 * projection) / math.pi

def main(tweets, boundaries, output, width):
    """
    Draws an image.
    This function creates an image object, constructs Region objects by reading
    in data from csv files, and draws polygons on the image based on those Regions
    Args:
        tweets (str): name of a csv file of hashtag instance coordinates    xxxxxelection tweetsxxxxx
        boundaries (str): name of a csv file of geographic information
        output (str): name of a file to save the image
        width (int): width of the image
    """
    with open(tweets, 'r') as tweet_file:
        tweet_file_list = list(csv.reader(tweet_file))
    with open(boundaries, 'r') as boundary_file:
        boundary_file_list = (list(csv.reader(boundary_file)))

    def to_point(boundary_file_list):
        """Takes a list of consecutive long,lat and returns a list of (long,lat)
        tuples, also mercator'ing the latitudinal coordinate.
        """
        point_list = list()
        for i in range(2, len(boundary_file_list), 2):
            point_list.append((float(boundary_file_list[i]), mercator(float(boundary_file_list[i+1]))))
        return point_list

    region_list = [Region(to_point(boundary)) for boundary in boundary_file_list]
    tweet_list = [Tweet(tweet_coord[0], mercator(float(tweet_coord[1])), POINT_RAD) for tweet_coord in tweet_file_list[1:]]

    min_long_list = [Region.min_long() for Region in region_list]
    max_long_list = [Region.max_long() for Region in region_list]
    min_lat_list = [Region.min_lat() for Region in region_list]
    max_lat_list = [Region.max_lat() for Region in region_list]

    plottah = Plot(width, min(min_long_list), min(min_lat_list), max(max_long_list), max(max_lat_list))

    for region in region_list:
        plottah.draw(region)

    tweet_num = 0
    total_num = len(tweet_list)
    for tweet in tweet_list:
        plottah.draw_tweet(tweet, tweet_num, total_num)
        tweet_num = tweet_num + 1

    plottah.save(output)

if __name__ == '__main__':
    tweets = sys.argv[1]
    boundaries = sys.argv[2]
    output = sys.argv[3]
    width = int(sys.argv[4])
    main(tweets, boundaries, output, width)
