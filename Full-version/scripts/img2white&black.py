from PIL import Image
import os

# Define the path to the input folder
input_folder = 'Test'

# Define the path to the output folder
output_folder = 'Testb&w'

# Loop through all files in the input folder
for folder in os.listdir(input_folder):
    for filename in os.listdir(input_folder + '/' + folder):
        # Open the image file
        with Image.open(os.path.join(input_folder, folder, filename)) as img:
            # Convert the image to black and white
            img = img.convert('L')
            # Define the path to the output file
            output_file = os.path.join(output_folder, folder, filename)
            # Save the black and white image
            img.save(output_file)
