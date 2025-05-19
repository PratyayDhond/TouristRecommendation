import math
import json
from datetime import datetime

def println(lines: int = 1):
    print("-------------------------------------------")
    printNewLine(lines)

def printNewLine(n : int):
    for i in range(0,n):
        print('\n')

def get_radius( lat_range: float, lon_range: float) -> float:

    if abs(lat_range) > abs(lon_range):
        return abs(lat_range)
    else:
        return abs(lon_range)

def get_json_data(file_path: str):
    json_data = []
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
        print("JSON loaded successfully:", json_data)
    except FileNotFoundError:
        print("Error: File not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")
    return json_data

def falls_in_range(image_data, tourist_place_data) -> bool:
    image_lat = image_data['lat']
    image_lon = image_data['lon']
    tourist_place_lat = tourist_place_data['lat']
    tourist_place_lon = tourist_place_data['lon']
    lat_diff = abs(image_lat - tourist_place_lat)
    lon_diff = abs(image_lon - tourist_place_lon)

    if lat_diff < tourist_place_data['lat_range'] and lon_diff < tourist_place_data['lon_range']:
        return True
    return False


def mins_since_midnight(timestamp: str) -> int:
    dt = datetime.strptime(timestamp, '%Y:%m:%d %H:%M:%S')
    minutes_since_midnight = dt.hour * 60 + dt.minute + dt.second / 60
    return int(minutes_since_midnight)

def image_time_sector(image_data) -> int:
    timestamp = mins_since_midnight(image_data['timestamp'])
    sector=-1
    if timestamp < 360:
        sector = 0
    elif timestamp < 720:
        sector = 1
    elif timestamp < 1080:
        sector = 2
    elif timestamp < 1440:
        sector = 3
    return sector


def get_time_sectors(start_time,end_time):
    no_of_time_sectors = 0
    start_sector = 0
    end_sector = 4
    if start_time < 360:
        start_sector = 0
    elif start_time < 720:
        start_sector = 1
    elif start_time < 1080:
        start_sector = 2
    elif start_time < 1440:
        start_sector = 3

    if end_time > 1080:
        end_sector = 3
    elif end_time > 720:
        end_sector = 2
    elif end_time > 360:
        end_sector = 1
    elif end_time > 0:
        end_sector = 0
        
    no_of_time_sectors = end_sector - start_sector + 1
    return no_of_time_sectors, start_sector, end_sector