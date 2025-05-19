import os

# Set your dataset directory path
dataset_dir = "./_geotagged_timestamped_images/"

# Define allowed image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

def count_images_in_directory(directory):
    image_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                image_count += 1
    return image_count

total_images = count_images_in_directory(dataset_dir)
print(f"Total number of images in the dataset: {total_images}")
