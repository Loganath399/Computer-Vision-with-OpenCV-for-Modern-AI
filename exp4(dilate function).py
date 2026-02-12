import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the image from given location
image_path = r"C:\Users\logan\OneDrive\Desktop\exp4.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if image is None:
    print("Error: Image not found at the given path")
    exit()

# Step 2: Create a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Step 3: Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Step 4: Display original and dilated images
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Dilated Image")
plt.imshow(dilated_image, cmap='gray')
plt.axis('off')

plt.show()
