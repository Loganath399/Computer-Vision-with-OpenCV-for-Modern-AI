import cv2
import numpy as np

# Full image path (update if needed)
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\OIP.jpg")

if img is None:
    print("Image not loaded. Check file name or path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X and Y Edge Detection
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Compute magnitude of gradients
sobel_magnitude = cv2.magnitude(sobelx, sobely)

# Convert to 8-bit image for display
sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

# Show result
cv2.imshow("Sobel XY Edge Detection", sobel_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
