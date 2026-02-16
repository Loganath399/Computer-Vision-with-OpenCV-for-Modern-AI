import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp4.png")

if img is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)

# Sobel Y
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

# Sobel XY (magnitude)
sobel_magnitude = cv2.magnitude(
    cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3),
    cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
)
sobel_magnitude = cv2.convertScaleAbs(sobel_magnitude)

# Laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Sobel XY (Magnitude)", sobel_magnitude)
cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
