from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb

class Plot:
    """
    Provides the ability to map, draw and color regions in a long/lat
    bounding box onto a proportionally scaled image.
    """
    @staticmethod
    def interpolate(x_1, x_2, x_3, newlength):
        """
        linearly interpolates x_2 <= x_1 <= x_3 into newlength.
        x_2 and x_3 define a line segment, and x1 falls somewhere between them.
        scale the width of the line segment to newlength, and return where
        x_1 falls on the scaled line.
        """
        length = (x_3) - (x_2)
        original_s1 = (x_1) - (x_2)
        ratio = float(original_s1/length)

        new_sl = float(ratio * newlength)
        return int(new_sl)

    @staticmethod
    def proportional_height(new_width, width, height):
        """
        return a height for new_width that is
        proportional to height with respect to width
        Yields:
            int: a new height
        """
        width_ratio = float(new_width / width)
        new_height = int(height * width_ratio)
        return new_height #why is new_height an int... heights/widths have to be ints?

    @staticmethod
    def fill(region, style):
        """return the fill color for region according to the given 'style'"""
        if style == "GRAD":
            return Plot.gradient(region)
        else:
            return Plot.solid(region)

    @staticmethod
    def solid(region):
        """
        a solid color based on a region's plurality of votes
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        if region.plurality() == 'REPUBLICAN':
            return (255, 0, 0)
        elif region.plurality() == 'DEMOCRAT':
            return(0, 0, 255)
        else:
            return (0, 255, 0)
    @staticmethod
    def gradient(region):
        """
        a gradient color based on percentages of votes in a region
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        red_val = int(region.republican_percentage() * 255)
        green_val = int(region.other_percentage() * 255)
        blue_val = int(region.democrat_percentage() * 255)
        return (red_val, green_val, blue_val)

    def __init__(self, width, min_long, min_lat, max_long, max_lat):
        """
        Create a width x height image where height is proportional to width
        with respect to the long/lat coordinates.
        """
        self.width = width
        self.min_long = min_long
        self.min_lat = min_lat
        self.max_long = max_long
        self.max_lat = max_lat
        self.original_width = self.max_long - self.min_long
        self.original_height = self.max_lat - self.min_lat
        self.height = Plot.proportional_height(self.width, self.original_width, self.original_height)
        self.image = Image.new("RGB", (self.width, self.height), (255, 255, 255))

    def save(self, filename):
        """save the current image to 'filename'"""
        self.image.save(filename, "PNG")

    def draw(self, region):
        """
        Draws 'region' in the given 'style' at the correct position on the
        current image
        Args:
            region (Region): a Region object with a set of coordinates
            style (str): 'GRAD' or 'SOLID' to determine the polygon's fill
        """
        def trans_long(): #x values
            long_list = [int(Plot.interpolate(long_coord, self.min_long, self.max_long, self.width)) for long_coord in region.longs()]
            return long_list

        def trans_lat(): #y values
            lat_list =  [int(Plot.interpolate(lat_coord, self.min_lat, self.max_lat, self.height)) for lat_coord in region.lats()]
            subtracted = [self.height - lat_value for lat_value in lat_list]
            return subtracted

        coord_list = [(x, y) for x, y in zip(trans_long(), trans_lat())]
        ImageDraw.Draw(self.image).polygon(coord_list, fill=None, outline='black')

    def draw_tweet(self, tweet, tweet_num, total_num):
        pold_tl_lon = int(Plot.interpolate(tweet.tl_lon, self.min_long, self.max_long, self.width))
        pold_tl_lat = self.height - int(Plot.interpolate(tweet.tl_lat, self.min_lat, self.max_lat, self.height))

        pold_br_lon = int(Plot.interpolate(tweet.br_lon, self.min_long, self.max_long, self.width))
        pold_br_lat = self.height - int(Plot.interpolate(tweet.br_lat, self.min_lat, self.max_lat, self.height))

        ImageDraw.Draw(self.image).ellipse([(pold_tl_lon,pold_tl_lat),(pold_br_lon,pold_br_lat)], fill=(int((255*(tweet_num/total_num))),0,255))
