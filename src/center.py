import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage


path='array.npy'



with open(path,'rb') as f:
    array2 = np.load(f)
    
def find_local_maxima(image):
  """
  Finds the local maxima in an image.

  Args:
    image: A NumPy array representing the image.

  Returns:
    A NumPy array of the coordinates of the local maxima.
  """

  # Create a mask of the local maxima.
  mask = np.zeros_like(image, dtype=bool)
  for i in range(1, 128- 1):
    for j in range(1, 128 - 1):
      if image[i, j] > image[i - 1, j] and image[i, j] > image[i + 1, j] and image[i, j] > image[i, j - 1] and image[i, j] > image[i, j + 1]:
        if image[i,j]>0.3:
          
            mask[i, j] = True

  # Return the coordinates of the local maxima.
  return np.where(mask)

local_max = find_local_maxima(array2[0])

plt.scatter(local_max[1], local_max[0], c='r')
plt.imshow(array2[0])
plt.show()


