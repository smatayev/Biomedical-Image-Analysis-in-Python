# Import ImageIO and NumPy
import imageio
import numpy as np

# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 = imageio.imread('chest-221.dcm')
im3 = imageio.imread('chest-222.dcm')

# Stack images into a volume
# By convention, volumetric data should be stacked along the first dimension: vol[plane, row, col]
# NumPy's stack() function to combine several 2D arrays into a 3D volume
vol = np.stack([im1, im2, im3]) 
print('Volume dimensions:', vol.shape)