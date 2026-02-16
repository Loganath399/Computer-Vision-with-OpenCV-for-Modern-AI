import cv2
import numpy as np

# Full image path (update if needed)
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\OIP.jpg")

if img is None:
    print("Image not loaded. Check file name or path.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel Y Edge Detection
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

# Show result
cv2.imshow("Sobel Y Edge Detection", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
