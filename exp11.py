import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp4.png")

if img is None:
    print("Error: Image not found")
    exit()

rows, cols = img.shape[:2]

# Define 3 points in the original image
pts1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Define corresponding 3 points in the output image
pts2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Compute affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
