import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import pandas as pd
import csv
import json
import sys

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (t, value) in GPSTAGS.items():
                if t in exif[idx]:
                    geotagging[value] = exif[idx][t]

    return geotagging

def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    try:
        # Check if all required keys are present
        if 'GPSLatitude' in geotags and 'GPSLongitude' in geotags and 'GPSLatitudeRef' in geotags and 'GPSLongitudeRef' in geotags:
            lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])
            lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])
            return lat, lon
        elif 'GPSLatitude' in geotags and 'GPSLongitude'in geotags:
            lat = get_decimal_from_dms(geotags['GPSLatitude'], 'E')
            lon = get_decimal_from_dms(geotags['GPSLongitude'], 'N')
            return lat, lon
        else:
            print("Missing required geotag information.")
            input()
            return None
    except Exception as e:
        print(f"Error extracting coordinates: {e}")
        input()
        return None


def write_to_csv(filename, data):
    df = pd.DataFrame(data, columns=['Image', 'lat', 'lon'])
    df.to_csv(filename, index=False)

def extract_geotagging_data(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    gps_info = {}
                    for gps_tag in value:
                        gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                        gps_info[gps_tag_name] = value[gps_tag]
                    return gps_info
    except Exception as e:
        print(f"Error: {e}")
        print(image_path)
    return None


print("Metadata extraction complete.")


data = []
print('Initialised data points array successfully...')


if not sys.stdin.isatty():  # Checks if stdin is redirected (called from subprocess)
    directory = sys.stdin.read().strip()
    print(f"Received directory from parent: {directory}")
else:
    directory = '../_geotagged_images'
# directory = '/home/dhondpratyay/adj/geotag/dataset/_geotagged_images'  # directory containing images

print('Selected Dataset Directory...')
print('Initiating image metadata extraction...')

for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    
    # Check if the path is a directory
    if os.path.isdir(subdir_path):
        print(f"Processing directory: {subdir_path}")
        
        # Loop through each file in the subdirectory
        for filename in os.listdir(subdir_path):
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
                file_path = os.path.join(subdir_path, filename)
                try:
                    image = Image.open(file_path)
                    exif = image._getexif()
                    geotags = extract_geotagging_data(file_path)
                    coordinates = get_coordinates(geotags)
                    
                    if coordinates is not None:
                        data.append([filename, *coordinates])
                except ValueError:
                    print(f"No geographic coordinates found for {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

data.sort()
print('Data sorted successfully...')
write_to_csv('coordinates.csv', data)
print('data converted and stored to coordinates.csv')
def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data_list = []

        for row in csv_reader:
            data_list.append({
                'Image': row['Image'],
                'lat': float(row['lat']),
                'lon': float(row['lon'])
            })

    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

csv_to_json('coordinates.csv', 'coordinates.json')
print('Data converted to json file successfully.')