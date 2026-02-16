import cv2
import numpy as np

# Full image path (update if needed)
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\OIP.jpg")

if img is None:
    print("Image not loaded. Check file name or path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X Edge Detection
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

# Show result
cv2.imshow("Sobel X Edge Detection", sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
