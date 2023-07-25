### resize
"""
from ImageImmunization.InputFeatures.ResizeImages import resize_and_save_images

input_directory = "tmp_dataset"
desired_output_size = (512, 512)

resize_and_save_images(input_directory, desired_output_size)
"""

### edge map
"""
from ImageImmunization.InputFeatures.CannyEdgeCreator import edge_detection_and_save

input_directory = "tmp_dataset/resized_512x512"
lower_thresh = 40
upper_thresh = 120
use_l2_norm = False

edge_detection_and_save(input_directory, lower_thresh, upper_thresh, use_l2_norm)
"""

# number of channels:
"""
import cv2


def check_edgemap_channels(edgemap_path):
    # Read the edgemap image using OpenCV
    edgemap = cv2.imread(edgemap_path, cv2.IMREAD_UNCHANGED)

    # Get the number of channels in the image
    num_channels = edgemap.shape[-1]

    if num_channels == 1:
        print("The edgemap is a one-channel (grayscale) image.")
    elif num_channels == 3:
        print("The edgemap is a three-channel (color) image.")
    else:
        print("The edgemap has an unexpected number of channels:", num_channels)

    print("edgemap.shape:", edgemap.shape)
    print("edgemap:", edgemap)

# Example usage:
edgemap_path = "tmp_dataset/resized_512x512/edge_maps_40-120_L1_norm/2_edge.jpg"
check_edgemap_channels(edgemap_path)
"""



