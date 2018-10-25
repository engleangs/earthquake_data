class EarthQuake:
    def __init__(self, date, time_utc, lat, lon, depth, depth_type, magnitude_type, magnitude, region_name, last_update,
                 eqid):
        self.date = date
        self.time_utc = time_utc
        self.lat = lat
        self.lon = lon
        self.depth = depth
        self.depth_type = depth_type
        self.magnitude = magnitude
        self.magnitude_type = magnitude_type
        self.region_name = region_name
        self.last_update = last_update
        self.eqid = eqid

    def __str__(self):
        return "date: " + self.date + ", time_utc :" + self.time_utc + ", latitude:" + str(
            self.lat) + ", longitude:" + str(self.lon) \
               + ",depth :" + str(self.depth) + ", depth_type : " + self.depth_type + ", magnitude :" + str(
            self.magnitude) \
               + ", magnitude_type :" + self.magnitude_type + ", region_name :" + self.region_name \
               + ", last_update :" + self.last_update + ", eqid : " + self.eqid


class EarthquakeFactory:
    @staticmethod
    def instance(text):
        data = str(text).split(";")
        date = data[0]
        time_utc = data[1]
        lat = float(data[2])
        lon = float(data[3])
        depth = float(data[4])
        depth_type = data[5]
        magnitude_type = data[6]
        magnitude = float(data[7])
        region_name = data[8]
        last_update = data[9]
        eqid = data[10]
        return EarthQuake(date, time_utc, lat, lon, depth, depth_type, magnitude_type, magnitude, region_name,
                          last_update, eqid)
