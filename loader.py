from earthquake import EarthquakeFactory


class Loader:
    def __init__(self, path):
        self.path = path

    def load(self):
        data = []
        line_number = 0
        with open(self.path, "r") as data_file:
            for line in data_file:
                if line_number > 0:
                    earthquake = EarthquakeFactory.instance(line)
                    data.append(earthquake)

                line_number = line_number + 1
        return data
