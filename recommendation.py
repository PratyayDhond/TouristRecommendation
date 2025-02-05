'''
1. Call the script that will extract geotags to a csv and json 
2. Read for the co-ordinates and ranges of places in the dataset
3. Read from the JSON file into current script
4. Determine how many points there are per place/co-ordiante
5. Set a default density preference
6. Give option to user for inputting density/distance preference
7. Generate a heatmap using MapBOX API or matplot, etc.
8. Recommend tourist place to user 

'''

import subprocess
import os
import json
import math
from _scripts.methods import println,get_json_data, falls_in_range
from flask import Flask, request, jsonify
from flask_cors import CORS


dir = "./_scripts/"  
script_name = "geotagToCsv.py"   
script_path = os.path.join(dir, script_name)
dataset_dir = "./_geotagged_images/"
subprocess.run(["python3", script_path], input=dataset_dir, text=True)

println()

print("Reading tourist location co-ordinates")

tourist_locations_file_name = 'touristLocationCoords.json'
file_path = "./" + tourist_locations_file_name
json_data = get_json_data(file_path)

println()
print("Creating Objects for tourists locations with respective range radius")

tourist_places_data = {}
for data in json_data:
    lat = data['lat']
    lon = data['lon']
    lat_range = data['lat_range']
    lon_range = data['lon_range']
    # radius = get_radius(data['lat_range'], data['lon_range'])
    tourist_places_data[data['name']] = {"lat":lat, "lon":lon, "lat_range": lat_range, "lon_range": lon_range, "density": 0}

print(tourist_places_data)

println()
'''
4. Reading from the geotagged dataset to determine density per location
'''
print("Reading location tags from the dataset")

geotagged_data_file_name = 'coordinates.json'
geotag_dataset_path = './' + geotagged_data_file_name
geotagged_data = get_json_data(geotag_dataset_path)

'''
At this point of code, We have,
- Tourist locations with their respective range radius
- Geotagged dataset with location tags
Now, next up our goal is to
- Calculate the distance between geotagged image locations and landmark/tourist locations
- Check if the image falls within the range of the current landmark
    - If TRUE -> Update Density by 1, skip iteration
    - If FALSE -> Continue
- Determine the density of geotagged images per tourist location
'''

for image_data in geotagged_data:
    for curr_tourist_place, curr_tourist_place_data in tourist_places_data.items():
        # Calculate the distance between geotagged image location and landmark/tourist location
        if falls_in_range(image_data, curr_tourist_place_data):
            # Update Density by 1 and skip for other tourist places
            # Should this be skipped in the future though? I don't know to be honest, what if it falls within range for two nearby tourist locations
            # Not a big concern as of now though #todo
            tourist_places_data[curr_tourist_place]['density'] += 1
            continue


println(2)
print("Density data has been prepared for tourist locations") 

densities = [place_data['density'] for place_data in tourist_places_data.values()]
min_dens = min(densities)
max_dens = max(densities)

for place, place_data in tourist_places_data.items():
    normalized_density = ((place_data['density'] - min_dens) / (max_dens - min_dens)) * 100
    tourist_places_data[place]['normalized_density'] = normalized_density


for curr_tourist_place, curr_tourist_place_data in tourist_places_data.items():
    print(curr_tourist_place + " : " + str(curr_tourist_place_data['density']) + " : " + str(curr_tourist_place_data['normalized_density']))



println()
print("Application has been initialised successfully")
print("Starting applicaiton server now..")

app = Flask(__name__)
CORS(app)

# To calculate distance in kilometers using Lat and lon values
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# Normalising the Density between a range of 0 to 100
@app.route('/all_locations', methods=['GET'])
def all_locations():
    # Extract all densities to find min and max
    densities = [place_data['density'] for place_data in tourist_places_data.values()]
    min_dens = min(densities)
    max_dens = max(densities)

    locations = [
        {
            'lat': place_data['lat'],
            'lon': place_data['lon'],
            'density': place_data['density'],
            'normalized_density': place_data['normalized_density'],
            'name': place
        }
        for place, place_data in tourist_places_data.items()
    ]

    return jsonify(locations)


# @app.route('/recommend', methods=['GET'])
# def recommend():
#     user_lat = float(request.args.get('lat'))
#     user_lon = float(request.args.get('lon'))
#     density_pref = int(request.args.get('density'))

#     filtered_places = []

#     for place, place_data in tourist_places_data.items():
#         if place_data['density'] <= density_pref:
#             curr_place = {'lat':place_data['lat'], 'lon':place_data['lon'], 'density':place_data['density'], 'name':place}
#             filtered_places.append(curr_place)

#     if len(filtered_places) > 0:
#         println()
#         print("Recommending nearest place from following places")
#         for place in filtered_places:
#             print(place['name'])
    
#     if not filtered_places:
#         return jsonify({"message": "No places match your density preference."})
    
#     nearest_place = min(filtered_places, key=lambda place: haversine(user_lat, user_lon, place['lat'], place['lon']))
#     print("Recommended place : " + nearest_place['name'])
#     return jsonify(nearest_place)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_lat = float(request.args.get('lat'))
    user_lon = float(request.args.get('lon'))
    min_density = int(request.args.get('min_density'))
    max_density = int(request.args.get('max_density'))
    num_recommendations = int(request.args.get('num'))

    filtered_places = [
        {
            'lat': place_data['lat'],
            'lon': place_data['lon'],
            'density': place_data['density'],
            'normalized_density': place_data['normalized_density'],
            'name': place
    }
        for place, place_data in tourist_places_data.items()
        if min_density <= place_data['normalized_density'] <= max_density
    ]

    if not filtered_places:
        return jsonify({"message": "No places match your density preference."})

    # Sort by distance and get top `num_recommendations`
    sorted_places = sorted(
        filtered_places,
        key=lambda place: haversine(user_lat, user_lon, place['lat'], place['lon'])
    )[:num_recommendations]



    return jsonify(sorted_places)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)



#  TODO -> Normalise the density (You can't have a place with 20 people and a place with 860 unless you normalise within a specific range)