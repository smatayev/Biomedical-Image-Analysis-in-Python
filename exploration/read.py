# imageio is a versatile package. It can read in a variety of image data, including JPEG, PNG, and TIFF. 
# But it's especially useful for its ability to handle DICOM files.

# Import ImageIO
import imageio

# Load "chest-220.dcm"
im = imageio.imread("chest-220.dcm" ) # ImageIO reads in data as Image objects. These are standard NumPy arrays with a dictionary of metadata.

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)

# Print the available metadata fields
print(im.meta.keys())

