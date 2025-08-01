# Import ImageIO
import imageio

# Load the "tcia-chest-ct" directory
vol = imageio.volread("tcia-chest-ct") 
# volread() function can load multi-dimensional datasets and create 3D volumes from a folder of images
# It also preserves image metadata where possible

# Print image attributes
print('Available metadata:', vol.meta.keys())
print('Shape of image array:', vol.shape)