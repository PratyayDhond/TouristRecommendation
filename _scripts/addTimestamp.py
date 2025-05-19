import os
import piexif
import random
from datetime import datetime, timedelta
from PIL import Image

def generate_random_timestamp(start_time, end_time):
    start = datetime.strptime(start_time, "%H:%M")
    end = datetime.strptime(end_time, "%H:%M")
    random_time = start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
    return random_time.strftime("%H:%M:%S")

def add_timestamp_to_metadata(input_dir, output_dir, start_time, end_time):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # random_days = random.randint(1,60)
    # date_today_minus_45 = (datetime.today() - timedelta(days=random_days)).strftime("%Y:%m:%d")
    print(input_dir)
    for root, _, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)
        output_subdir = os.path.join(output_dir, relative_path)

        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # timestamp_ranges = [{"start_time":"00:00", "end_time":"06:00"},{"start_time":"12:00", "end_time":"18:00"},{"start_time":"18:00", "end_time":"23:59"},{"start_time":"18:00", "end_time":"23:59"}]
        for file in files:

            random_days = random.randint(1,60)
            date_today_minus_45 = (datetime.today() - timedelta(days=random_days)).strftime("%Y:%m:%d")

            if file.lower().endswith(('jpg', 'jpeg')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, file)
                
                try:
                    img = Image.open(input_path)
                    exif_dict = piexif.load(img.info.get("exif", b""))
                    
                    # Generate a random timestamp within the specified range
                    
                    # time_stamp_range_rand_selector = random.randint(0,3)
                    # time_component = generate_random_timestamp(timestamp_ranges[time_stamp_range_rand_selector]["start_time"], timestamp_ranges[time_stamp_range_rand_selector]["end_time"])
                    time_component = generate_random_timestamp("06:00","12:00")
                    timestamp = f"{date_today_minus_45} {time_component}"
                    
                    # Set the DateTimeOriginal and DateTimeDigitized fields
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = timestamp.encode()
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = timestamp.encode()
                    
                    # Convert exif back to bytes
                    exif_bytes = piexif.dump(exif_dict)
                    
                    # Save image with modified metadata
                    img.save(output_path, "jpeg", exif=exif_bytes)
                    print(f"Processed: {output_path} with timestamp {timestamp}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    input_directory = "._geotagged_images"
    output_directory = "_geotagged_timestamped_images"
    start_time_range = "06:00"  # Start of the range (6 AM)
    end_time_range = "12:00"    # End of the range (12 Noon)
    add_timestamp_to_metadata(input_directory, output_directory, start_time_range, end_time_range)