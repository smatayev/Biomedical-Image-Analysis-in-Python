# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread("chest-220.dcm")

#===========

# Draw the image in grayscale
plt.imshow(im, cmap="gray") #cmap controls the color mappings for each value

# Render the image
plt.show()

#===========

# Draw the image with greater contrast
plt.imshow(im, cmap="gray", vmin=-200, vmax=200) #vmin and vmax control the color contrast between values. Changing these can reduce the influence of extreme values.

plt.axis('off') #removes axis and tick labels from the image.

# Render the image
plt.show()

#===========

