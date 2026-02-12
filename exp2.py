import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp2.png")

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply Gaussian Blur
# (kernel size must be odd, e.g., 3x3, 5x5, 7x7)
blur_image = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# Display Original and Blurred images
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gaussian Blurred Image")
plt.imshow(blur_image)
plt.axis("off")

plt.show()
