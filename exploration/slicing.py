# Import PyPlot
import matplotlib.pyplot as plt

# ===========

# Initialize figure and axes grid
fig, axes = plt.subplots(nrows=2, ncols=1)

# Plotting many slices sequentially can create a "fly-through" effect that helps you understand the image as a whole.

vol = imageio.volread('chest-data')

# Draw an image on each subplot
axes[0].imshow(im1, cmap="gray")
axes[1].imshow(im2, cmap="gray")

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()

# ============

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=1, ncols=4)

vol = imageio.volread('chest-data')

# Loop through subplots and draw image
for ii in range(4):
    im = vol[ii*40,:,:]
    axes[ii].imshow(im, cmap='gray')
    axes[ii].axis('off')
    
# Render the figure
plt.show()

# ============= Changing Aspect Ratios for different perspectives

# Any two dimensions of an array can form an image, and slicing 
# along different axes can provide a useful perspective (axial, coronal, saggital). 
# However, unequal sampling rates can create distorted images.
# Changing the aspect ratio can address this by increasing the width of one of the dimensions

# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray', aspect=asp1)
axes[1].imshow(im2, cmap='gray', aspect=asp2)
plt.show()
