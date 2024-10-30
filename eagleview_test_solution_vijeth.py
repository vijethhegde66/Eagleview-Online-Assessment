import cv2
import numpy as np
import os
from concurrent.futures import ThreadPoolExecutor
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class ImageProcessor:
    def __init__(self, file_paths, output_dir):
        print(file_paths)
        ###################filtering outh the pnj file form jpg in the given folder##############
        self.file_paths = [
        os.path.join(file_paths, filename) 
        for filename in os.listdir(file_paths) 
        if filename.lower().endswith(".jpg")
        ]
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _create_mask(self, file_path):

        # Loading the file from the path specified
        image = cv2.imread(file_path)
        
        # verifying the images in the path
        if image is None:
            logging.error(f"Error: Unable to load image '{file_path}'.")
            return 0

        # Generate binary mask for high-intensity regions
        mask = cv2.inRange(image, (200, 200, 200), (255, 255, 255))
        
        # counting no of images with the high instyensity pixel count
        pixel_count = np.sum(mask == 255)

        # Saving the resultant or masked images
        output_path = os.path.join(
            self.output_dir,
            os.path.basename(file_path).replace(".jpg", "_mask.png")
        )
        cv2.imwrite(output_path, mask)

        return pixel_count
#################################parallel processing the images from the path###############
    def process_images(self):

        with ThreadPoolExecutor() as executor:
            pixel_counts = list(executor.map(self._create_mask, self.file_paths))

        # Calculate and log the total pixel count
        total_pixel_count = sum(pixel_counts)
        logging.info(f"Total high-intensity pixel count: {total_pixel_count}")
########################returing the total pixel count from the masked image########
        return total_pixel_count

if __name__ == "__main__":

    repo_root = os.getcwd()
    print(repo_root)
    image_dir = os.path.join(repo_root, 'images')
    print(image_dir)
    output_dir = os.path.join(repo_root, 'output_masks')

    processor = ImageProcessor(image_dir, output_dir)
    processor.process_images()
