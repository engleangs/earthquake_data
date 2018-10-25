class EarthQuake:
    def __init__(self,date,time_utc, lat,lon,depth,depth_type,magnitude_type,magnitude,region_name,last_update,eqid ):
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

class EarthquakeFactory:
    def Instance(self,text):
        data = str(text).split(";")
        str_date = data[0] + " "+ data[1]

