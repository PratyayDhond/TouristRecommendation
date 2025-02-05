import os
import requests
from PIL import Image
import piexif
import piexif.helper
from io import BytesIO

# Google Places API key
API_KEY = "AIzaSyBIm-ek6rDQ2-yYnCHLKp2dvjK0rITz5dg"

def get_places_nearby(location, radius=1000, place_type="restaurant", limit=10):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        # "type": place_type, type is reducing the number of possible images returned
        "key": API_KEY,
    }
    
    results = []
    while len(results) < limit:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Add new results, ensuring we don't exceed the limit
        results.extend(data.get("results", []))
        if "next_page_token" not in data or len(results) >= limit:
            break
        
        # Update parameters for the next page
        params["pagetoken"] = data["next_page_token"]

    return results[:limit]  # Return only the requested number of results

# Function to convert latitude and longitude to EXIF format
def convert_to_exif_format(coord):
    # Convert to degrees, minutes, and seconds
    degrees = int(coord)
    minutes = int((coord - degrees) * 60)
    seconds = round((coord - degrees - minutes / 60) * 3600, 5)
    return [(degrees, 1), (minutes, 1), (int(seconds * 100), 100)]

# Function to embed geotag data into an image
def embed_geotag(image_data, latitude, longitude, output_path):
    exif_dict = {"GPS": {}}
    
    # Set GPS latitude
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = convert_to_exif_format(abs(latitude))
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = "N" if latitude >= 0 else "S"
    
    # Set GPS longitude
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = convert_to_exif_format(abs(longitude))
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = "E" if longitude >= 0 else "W"
    
    # Create EXIF data and save to the image
    exif_bytes = piexif.dump(exif_dict)
    with Image.open(BytesIO(image_data)) as img:
        img.save(output_path, exif=exif_bytes)
    print(f"Geotagged image saved: {output_path}")

# Function to download a photo and embed geotag data
def download_photo(photo_reference, latitude, longitude, output_folder, max_width=400):
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "photoreference": photo_reference,
        "maxwidth": max_width,
        "key": API_KEY,
    }
    response = requests.get(url, params=params, stream=True)
    response.raise_for_status()

    # Embed geotag data and save the image
    photo_path = os.path.join(output_folder, f"{photo_reference}.jpg")
    embed_geotag(response.content, latitude, longitude, photo_path)

# Main function
def main():
    place_type = "tourist_attraction"
    max_images = 919  # Set a limit for the number of images to download
    places = [
        {
            "name": "Shaniwar Wada",
            "location": "18.519236,73.855511",
            "radius": 500,
            "limit": 919
        },
        {
            "name": "Dagdusheth",
            "location": "18.516405392620992, 73.85617561091513",
            "radius": 250,
            "limit": 806
        },
        {
            "name": "Sinhagadh Fort",
            "location": "18.36640935290076, 73.75593133885434",
            "radius": 750,
            "limit": 679
        },
        {
            "name": "Parvati Hill",
            "location": "18.494927697847487, 73.8443332445509",
            "radius": 500,
            "limit": 594
        },
        {
            "name": "Lonavala",
            "location": "18.75411042620645, 73.40760167342519",
            "radius": 1500,
            "limit": 509
        },
        {
            "name": "pLDeshpandeGarden",
            "location": "18.491193007172804, 73.83687185913749",
            "radius": 250,
            "limit": 424
        },
        {
            "name": "Pataleshwar Caves",
            "location": "18.527063829211222, 73.84984584750792",
            "radius": 300,
            "limit": 340
        },
        {
            "name": "Raigad Fort",
            "location": "18.233457692679917, 73.44070102351087",
            "radius": 1500,
            "limit": 255
        },
        {
            "name": "Torna Fort",
            "location": "18.27859706330615, 73.6217725351014",
            "radius": 1500,
            "limit": 170
        },
        {
            "name": "ISKCON Templ",
            "location": "18.448191578166302, 73.8804222436855",
            "radius": 800,
            "limit": 127
        },
        {
            "name": "KhadakWasla",
            "location": "18.43752671902905, 73.77121657684465",
            "radius": 500,
            "limit": 85
        },
        {
            "name": "KhadakWasla",
            "location": "18.44550062761074, 73.76326537321208",
            "radius": 500,
            "limit": 85
        },
        {
            "name": "Baner Hill",
            "location": "18.554843427136237, 73.78994228895327",
            "radius": 500,
            "limit": 42
        },
        {
            "name": "ARAI Hills",
            "location": "18.522253578937335, 73.81368566400259",
            "radius": 500,
            "limit": 25
        },
        {
            "name": "Simbi Tekdi",
            "location": "18.524757792143603, 73.82868402382914",
            "radius": 500,
            "limit": 17
        },
        {
            "name": "Lal Mahal",
            "location": "18.51891686922434, 73.85660838274482",
            "radius": 500,
            "limit": 38
        },
        {
            "name": "Shaniwar Wada",
            "location": "18.519236,73.855511",
            "radius": 500,
            "limit": 919
        },

    ]

    for place in places:
        location = place["location"]
        radius = place["radius"]
        output_folder = place["name"]

        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Get places nearby
        nearby_places = get_places_nearby(location, radius, place_type, max_images)

        # Download photos for each place (up to the limit)
        images_downloaded = 0
        for nearby_place in nearby_places:
            if images_downloaded >= max_images:
                break

            photos = nearby_place.get("photos", [])
            if photos:
                photo_reference = photos[0]["photo_reference"]
                latitude = nearby_place["geometry"]["location"]["lat"]
                longitude = nearby_place["geometry"]["location"]["lng"]
                download_photo(photo_reference, latitude, longitude, output_folder)
                images_downloaded += 1

if __name__ == "__main__":
    main()
