from PIL import Image
import os

# Set the desired image size
target_size = (524, 524)

# Set the image format
target_format = 'RGB'
cwd = os.getcwd()
relative_path = "dataset"
dataset_folder = os.path.join(cwd, relative_path)

for filename in os.listdir(dataset_folder):
    # Open the image file
    image_path = os.path.join(dataset_folder, filename)
    with Image.open(image_path) as image:
        # Convert the image to the target format
        image = image.convert(target_format)

        # Resize the image to the target size
        image = image.resize(target_size)

        # Save the preprocessed image
        save_path = os.path.join(dataset_folder, filename)
        image.save(save_path)


