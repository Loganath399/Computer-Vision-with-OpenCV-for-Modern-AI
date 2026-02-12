import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp3.png")

if img is None:
    print("Error: Image not found")
    exit()

rows, cols = img.shape[:2]

# Define 4 points in the original image (source points)
pts1 = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

# Define 4 corresponding points in the output image (destination points)
pts2 = np.float32([
    [10, 100],
    [280, 50],
    [50, 280],
    [300, 300]
])

# Compute perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_img = cv2.warpPerspective(img, M, (cols, rows))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
