class Region:
    """
    A region (represented by a list of long/lat coordinates) xxxxxalong with
    republican, democrat, and other vote counts.xxxxx

    TODO: Store sorted list of each coord to prevent repeated sorting.
    """
    def __init__(self, coords):
        self.coords = coords

    def lats(self):
        "Return a list of the latitudes of all the coordinates in the region"
        lat_list = [coord[1] for coord in self.coords]
        return lat_list
    def longs(self):
        "Return a list of the longitudes of all the coordinates in the region"
        long_list = [coord[0] for coord in self.coords]
        return long_list
    def min_lat(self):
        "Return the minimum latitude of the region"
        sorted_lats_for_min = sorted(self.lats()) #uses python default sort algorithm... what is it?
        return sorted_lats_for_min[0]
    def min_long(self):
        "Return the minimum longitude of the region"
        sorted_longs_for_min = sorted(self.longs())
        return sorted_longs_for_min[0]
    def max_lat(self):
        "Return the maximum latitude of the region"
        sorted_lats_for_max = sorted(self.lats())
        return sorted_lats_for_max[-1]
    def max_long(self):
        "Return the maximum longitude of the region"
        sorted_longs_for_max = sorted(self.longs())
        return sorted_longs_for_max[-1]
