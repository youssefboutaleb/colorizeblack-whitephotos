import os
from PIL import Image
from datasets import load_dataset
from google.colab import files
import shutil

dataset = load_dataset("huggingnft/cryptopunks")

# Specify the desired width and height
width = 256
height = 256

# Create a directory to store the resized images
os.makedirs("resized_images", exist_ok=True)

# Loop over the dataset and resize the images
for example in dataset["train"]:
    # Open the image directly from the PngImageFile object
    img = example["image"]
    
    # Resize the image
    img = img.resize((width, height))
    
    # Save the resized image to the new directory
    img.save(os.path.join("resized_images", f"{example['id']}.png"))

#download the dataset
shutil.make_archive('resized_images', 'zip', '/content/resized_images')
files.download('resized_images.zip')
