import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread(r'C:\Users\logan\OneDrive\Desktop\tree.png', 0)

# Define kernel (structuring element)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Apply Closing (dilation followed by erosion)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
