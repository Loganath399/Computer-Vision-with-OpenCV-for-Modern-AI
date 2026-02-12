import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define image path
image_path = r"C:\Users\logan\OneDrive\Desktop\exp5.png"

# Step 2: Read the image (color)
original_image = cv2.imread(image_path)

# Check if image is loaded
if original_image is None:
    print("Error: Image not found at the given path")
    exit()

# Convert BGR to RGB for display
original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# Step 3: Create structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Step 4: Apply erosion on color image
eroded_image = cv2.erode(original_image, kernel, iterations=1)

# Convert eroded image to RGB for display
eroded_rgb = cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB)

# Step 5: Display results
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.title("Original Color Image")
plt.imshow(original_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Eroded Color Image")
plt.imshow(eroded_rgb)
plt.axis('off')

plt.show()
