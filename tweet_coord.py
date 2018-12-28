class Tweet:

    def __init__(self, lon, lat, point_rad):
        """Initializes Tweet class instance, creating 4 ellipse coords from the given ellipse coord.
        """
        self.point_rad = point_rad
        self.lon = float(lon)
        self.lat = float(lat)
        self.tl_lon = (self.lon - self.point_rad)
        self.tl_lat = (self.lat + self.point_rad)
        self.br_lon = (self.lon + self.point_rad)
        self.br_lat = (self.lat - self.point_rad)
