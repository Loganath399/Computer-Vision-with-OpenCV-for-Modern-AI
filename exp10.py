import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp5.png")

if img is None:
    print("Error: Image not found")
    exit()

# Get image size
rows, cols = img.shape[:2]

# Define translation values
tx = 100   # move right by 100 pixels
ty = 50    # move down by 50 pixels

# Create translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
translated_img = cv2.warpAffine(img, M, (cols, rows))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
