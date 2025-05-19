import os
import random
from PIL import Image
import piexif

def add_geotag_to_image(image_path, output_path, base_lat, base_lon, range_lat, range_lon):
    """
    Adds a geotag with random variations to an image's metadata.

    :param image_path: Path to the input image.
    :param output_path: Path to save the geotagged image.
    :param base_lat: Base latitude.
    :param base_lon: Base longitude.
    :param range_lat: Range for randomness in latitude.
    :param range_lon: Range for randomness in longitude.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        if not os.path.exists(image_path):
            print(f"File does not exist: {image_path}")
            return

        print(f"Current working directory: {os.getcwd()}")

        # Generate random variations for the latitude and longitude
        rand_lat = base_lat + random.uniform(-range_lat, range_lat)
        rand_lon = base_lon + random.uniform(-range_lon, range_lon)

        # Convert latitude and longitude to EXIF format
        def to_exif_coord(value):
            degrees = int(abs(value))
            minutes = int((abs(value) - degrees) * 60)
            seconds = round((abs(value) - degrees - minutes / 60) * 3600, 6)
            return degrees, minutes, seconds

        lat_deg, lat_min, lat_sec = to_exif_coord(rand_lat)
        lon_deg, lon_min, lon_sec = to_exif_coord(rand_lon)

        # Define GPS tags
        gps_ifd = {
            piexif.GPSIFD.GPSLatitudeRef: "N" if rand_lat >= 0 else "S",
            piexif.GPSIFD.GPSLatitude: [(lat_deg, 1), (lat_min, 1), (int(lat_sec * 1000000), 1000000)],
            piexif.GPSIFD.GPSLongitudeRef: "E" if rand_lon >= 0 else "W",
            piexif.GPSIFD.GPSLongitude: [(lon_deg, 1), (lon_min, 1), (int(lon_sec * 1000000), 1000000)],
        }

        # Load existing EXIF data or initialize an empty dictionary

        exif_dict = {}
        try:
            exif_dict = piexif.load(img.info.get("exif", b""))
        except Exception:
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
            
        exif_dict["GPS"] = gps_ifd
        exif_bytes = piexif.dump(exif_dict)

        # Save the image with updated EXIF data
        img.save(output_path, "jpeg", exif=exif_bytes)
        print(f"Geotag added to {output_path}: ({rand_lat}, {rand_lon})")

    except Exception as e:
        print(f"Failed to add geotag to {image_path}: {e}")


def process_directories(dir_list, output_directory):
    """
    Processes a list of directories to append geotags to all images within them.

    :param dir_list: List containing tuples of (directory_name, latitude, longitude, range_lat, range_lon).
    :param output_directory: Directory to save geotagged images.
    """
    for directory_name, base_lat, base_lon, range_lat, range_lon in dir_list:
        output_subdir = os.path.join(output_directory, os.path.basename(directory_name))
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for filename in os.listdir(directory_name):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(directory_name, filename)
                output_path = os.path.join(output_subdir, filename)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                add_geotag_to_image(input_path, output_path, base_lat, base_lon, range_lat, range_lon)

# Example usage
if __name__ == "__main__":
    directories_data = [
        ("kasabaGanapatiMandir", 18.51904892027952, 73.85732014371902, .000004774939860, .00009927517845),  # Example directory and coordinates with range
        ("lalMahal", 18.518749353143637, 73.85663804005141, .000013113969402, .00014225236981),
        ("omkareshwarMandir", 18.51991941165052, 73.84896191802376, .000137774337748, .00023657649592),
        ("parvati", 18.495022999144158, 73.84410593369981, .000540865057516,.00158805655411),
        ("ramMandir", 18.511206166694222, 73.86943071768538, .00001603432467, .00007720892863),
        ("shaniwarWada", 18.519395968732155, 73.85536081497682, .000112924622915, .00074630751423),
        ("arai", 18.52666352568133, 73.81593046427638, .004971681030407, .00104869854812),
        ("Dagdusheth", 18.516327109348982, 73.8559085065869, .000167179971989, .00029751759885),
        ("isckonKatraj", 18.448299333294347, 73.88087331904809, .001180591337910, .00013411045111),
        ("pataleshwarCaves", 18.52694402291864, 73.85008588402799, .00000578760571, .00020753419499),
        ("raigadh", 18.233767433620244, 73.44090203395743, .000598809492536, .00036275610643),
        ("torna", 18.27594154497545, 73.62246386884068, .000041288682065, .00018967938748),
        ("banerHill", 18.554478545070893, 73.78987425655838, .000948152898100, .00144464864472),
        ("khadakwasla", 18.43529941252695, 73.77120237294524, .000843382568016, .00195581604183),
        ("pLDeshpandeGarden", 18.491412661460814, 73.83710835767204, .001119244739798, .00090122222444 ),
        ("simbiTekdi", 18.524104519030036, 73.83087105074793,.000030518929904, .00115871428858),
        ("sinhagadhFort", 18.366325678070964, 73.75582139099967, .000063640030276, .00140817113587)
    ]
    output_dir = "geotagged_images"  # Directory to save geotagged images

    process_directories(directories_data, output_dir)
