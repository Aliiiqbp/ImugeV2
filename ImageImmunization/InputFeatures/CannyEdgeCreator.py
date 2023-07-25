import os
import cv2


def edge_detection_and_save(input_dir, lower_threshold, upper_threshold, use_l2_norm=False):
    """
    Apply Canny edge detection to images in the input directory and save the edge maps.

    Parameters:
        1 - input_dir (str): Path to the directory with input images.

        2 - lower_threshold (int): Lower threshold for Canny edge detector.
        3 - upper_threshold (int): Upper threshold for Canny edge detector.
            - Recommended ratio: 1:2 to 1:3 (Lower: 30-50, Upper: 60-100)
            - Adjust based on noise and edge thickness preferences.
            - Lower Threshold: Affects sensitivity to detect weak edges and noise. Increase for images with more
            noise or thicker edges.
            - Upper Threshold: Influences how strong edges are detected. Decrease for images with finer and more
            precise edges in cleaner backgrounds.

        4 - use_l2_norm (bool, optional): True > Use L2-norm for gradient computation. False > Use L1-norm (default).
            - L1 norm: Thicker edges, robust to noise.
            - L2 norm: Thinner edges, precise in cleaner images.

    Returns:
        1 - None: Edge maps are saved in the "edge maps" folder inside the input directory.
    """

    l_norm_name = "L2_norm" if use_l2_norm else "L1_norm"
    folder_name = f"edge_maps_{lower_threshold}-{upper_threshold}_{l_norm_name}"
    output_dir = os.path.join(input_dir, folder_name)
    os.makedirs(output_dir, exist_ok=True)

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if use_l2_norm:
            edges = cv2.Canny(image, lower_threshold, upper_threshold, L2gradient=True)
        else:
            edges = cv2.Canny(image, lower_threshold, upper_threshold, L2gradient=False)

        output_file = os.path.join(output_dir, image_file.replace('.', '_edge.'))
        cv2.imwrite(output_file, edges)

    print("Edge maps saved successfully.")


"""
Example usage:

input_directory = "path/to/your/input_directory"
lower_thresh = 100
upper_thresh = 200
use_l2_norm = False

edge_detection_and_save(input_directory, lower_thresh, upper_thresh, use_l2_norm)
"""
