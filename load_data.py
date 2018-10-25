from pathlib import Path
from earthquake import EarthquakeFactory, EarthQuake

file_path = str(Path.cwd()) + "/data/export_EMSC.csv"
data = []
line_number = 0
with open(file_path, "r") as data_file:
    for line in data_file:
        if line_number > 0:
            earthquake = EarthquakeFactory.instance(line)
            data.append(earthquake)

        line_number = line_number + 1

for earthquake in data:
    print(earthquake)

