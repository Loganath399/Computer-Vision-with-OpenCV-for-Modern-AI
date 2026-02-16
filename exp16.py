import cv2
import numpy as np

# Load the image from your given path
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp3.png")

# Check if image is loaded properly
if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    # Scale up (double size)
    bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Scale down (half size)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Function to resize any image to a target height while preserving aspect ratio
    def resize_to_height(image, height):
        scale = height / image.shape[0]
        width = int(image.shape[1] * scale)
        return cv2.resize(image, (width, height))

    # Use original image height as target
    target_height = img.shape[0]
    smaller_resized = resize_to_height(smaller, target_height)
    bigger_resized = resize_to_height(bigger, target_height)

    # Now stack horizontally (all same height)
    comparison = np.hstack((smaller_resized, img, bigger_resized))

    # Display results
    cv2.imshow("Comparison: Smaller | Original | Bigger", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
