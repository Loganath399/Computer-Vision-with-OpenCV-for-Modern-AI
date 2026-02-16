import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread(r'C:\Users\logan\OneDrive\Desktop\tree.png', 0)

# Define the kernel (structuring element)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Apply Opening (erosion followed by dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display results
cv2.imshow('Original', img)
cv2.imshow('Opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
