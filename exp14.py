import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\tree.png")

if img is None:
    print("Error: Image not found")
    exit()

rows, cols = img.shape[:2]

# Define 4 source points (from original image)
src_pts = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

# Define 4 destination points (new perspective)
dst_pts = np.float32([
    [10, 100],
    [280, 50],
    [80, 300],
    [320, 280]
])

# Compute homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply homography transformation
homography_img = cv2.warpPerspective(img, H, (cols, rows))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
