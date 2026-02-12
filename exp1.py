import cv2
import matplotlib.pyplot as plt

# Load image using OpenCV
# Note: OpenCV loads images in BGR format
image = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\tree.png")

# Convert BGR to RGB for correct display in matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show side by side
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Grayscale")
plt.imshow(gray_image, cmap="gray")
plt.axis("off")

plt.show()
