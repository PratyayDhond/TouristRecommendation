import os
import requests

# Google Places API key
API_KEY = "AIzaSyBIm-ek6rDQ2-yYnCHLKp2dvjK0rITz5dg"

# Function to search for places near a location
def get_places_nearby(location, radius=1000, place_type="restaurant"):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "type": place_type,
        "key": API_KEY,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("results", [])

# Function to download a photo using the Google Places API photo endpoint
def download_photo(photo_reference, output_folder, max_width=400):
    url = f"https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "photoreference": photo_reference,
        "maxwidth": max_width,
        "key": API_KEY,
    }
    response = requests.get(url, params=params, stream=True)
    response.raise_for_status()

    # Save the image locally
    photo_path = os.path.join(output_folder, f"{photo_reference}.jpg")
    with open(photo_path, "wb") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)
    print(f"Downloaded: {photo_path}")

# Main function
def main():

    place_type = "tourist_attraction" 
    places = [
    {
        "name": "Shaniwar Wada",
        "location": "18.519236, 73.855511",
        "radius": 250,
    }
    ]

    print(places)
    print(places[0])
    print(places[0]['name'])

    location = places[0]['location'] # Example: San Francisco (latitude,longitude)
    radius = places[0]['radius']  # Search radius in meters
    place_type = place_type  # Type of places to search
    output_folder = places[0]['name']  # Folder to save images

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get places nearby
    places = get_places_nearby(location, radius, place_type)

    # Download photos for each place
    for place in places:
        photos = place.get("photos", [])
        if photos:
            photo_reference = photos[0]["photo_reference"]
            download_photo(photo_reference, output_folder)

if __name__ == "__main__":
    main()
