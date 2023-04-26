from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

# Set the directory containing the train folders
train_dir = '/content/colorizeblack-whitephotos/Beta-version/Train/'

# Load the images from each train folder
X = []
for i in range(8):
    folder_path = os.path.join(train_dir, f'Train{i}')
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            img = load_img(os.path.join(folder_path, filename))
            X.append(img_to_array(img))


# Convert the list of images to a numpy array
X = np.array(X, dtype=float)
