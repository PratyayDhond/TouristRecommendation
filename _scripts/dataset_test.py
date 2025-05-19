import os
import exifread
from collections import defaultdict
from datetime import datetime

# Define the base directory
base_dir = "_geotagged_timestamped_images"
totalCount = 0

# Time ranges
time_ranges = {
    "00:00 to 05:59": (0, 5),
    "06:00 to 11:59": (6, 11),
    "12:00 to 17:59": (12, 17),
    "18:00 to 23:59": (18, 23),
}

def get_exif_data(image_path):
    """Extracts the timestamp from image metadata."""
    with open(image_path, "rb") as f:
        tags = exifread.process_file(f, stop_tag="EXIF DateTimeOriginal", details=False)

    date_str = tags.get("EXIF DateTimeOriginal")
    if date_str:
        try:
            dt = datetime.strptime(str(date_str), "%Y:%m:%d %H:%M:%S")
            return dt.hour  # Extract only the hour
        except ValueError:
            return None
    return None

def categorize_images():
    """Reads images, extracts timestamps, and counts occurrences in time zones."""
    subdir_counts = defaultdict(lambda: {key: 0 for key in time_ranges})
    global totalCount  # Declare the global variable

    for subdir, _, files in os.walk(base_dir):
        if subdir == base_dir:  # Skip root folder itself
            continue

        subdir_name = os.path.basename(subdir)
        print(subdir_name)
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(subdir, file)
                hour = get_exif_data(image_path)
                totalCount += 1

                if hour is not None:
                    for label, (start, end) in time_ranges.items():
                        if start <= hour <= end:
                            subdir_counts[subdir_name][label] += 1
                            break

    return subdir_counts

# Run the categorization
image_counts = categorize_images()

# Print results
for subdir, counts in image_counts.items():
    print(f"\nSub-directory: {subdir}")
    for label, count in counts.items():
        print(f"  {label}: {count}")
    print(f"Dataset Size: {totalCount}")
