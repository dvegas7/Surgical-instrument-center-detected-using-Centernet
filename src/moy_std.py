import numpy as np
import cv2
import os



def compute_mean_std(image_dir):
    # List all image files in the specified directory
    image_files = os.listdir(image_dir)
    num_images = len(image_files)
    
    # Initialize variables to accumulate sums of pixel values and squares of pixel values
    sum_values = np.zeros((1, 1, 3))
    sum_squares = np.zeros((1, 1, 3))

    # Loop through each image file in the directory
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        image = cv2.imread(image_path)  # Load the image
        image = image.astype(np.float32) / 255.0  # Convert pixel values to floating point between 0 and 1

        # Accumulate sums of pixel values and squares of pixel values
        sum_values += np.sum(image, axis=(0, 1))
        sum_squares += np.sum(image ** 2, axis=(0, 1))

    # Calculate the mean and standard deviation
    mean = sum_values / (num_images * image.shape[0] * image.shape[1])
    std = np.sqrt(sum_squares / (num_images * image.shape[0] * image.shape[1]) - mean ** 2)


    # Round the mean and standard deviation to three decimal places
    mean_rounded = np.round(mean, 3)
    std_rounded = np.round(std, 3)

    return mean, std, mean_rounded, std_rounded

# Example of usage:
image_directory = '../data/instrument/image'
mean, std, mean_rounded, std_rounded = compute_mean_std(image_directory)

print('Mean:', mean)
print('Std:', std)
print('Mean rounded:', mean_rounded)
print('Std rounded:', std_rounded)

