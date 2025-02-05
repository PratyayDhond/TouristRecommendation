import math
import json

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
