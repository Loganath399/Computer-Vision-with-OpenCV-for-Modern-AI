import cv2

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp2.png")

if img is None:
    print("Error: Image not found")
    exit()

# Scale up (Bigger image)
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Scale down (Smaller image)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
