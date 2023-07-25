import os
import cv2


def resize_and_save_images(input_dir, output_size=(128, 128)):
    """
    Resize images in the input directory to a desired size and save them in a new folder.

    Parameters:
        input_dir (str): Path to the directory with input images.
        output_size (tuple, optional): Desired output size (width, height). Default: (128, 128).

    Returns:
        None: Resized images are saved in "resized_widthxheight" folder inside the input directory.

    Example Usage:
        input_directory = "path/to/your/input_directory"
        desired_output_size = (256, 256)

        resize_and_save_images(input_directory, desired_output_size)
    """

    output_folder_name = f"resized_{output_size[0]}x{output_size[1]}"
    output_dir = os.path.join(input_dir, output_folder_name)
    os.makedirs(output_dir, exist_ok=True)

    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        image = cv2.imread(image_path)

        resized_image = cv2.resize(image, output_size)

        output_file = os.path.join(output_dir, image_file)
        cv2.imwrite(output_file, resized_image)

    print(f"Images resized to {output_size[0]}x{output_size[1]} and saved in {output_folder_name} folder.")


