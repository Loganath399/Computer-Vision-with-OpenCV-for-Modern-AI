import cv2

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\tree.png")

if img is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Counter-clockwise rotation (45 degrees)
ccw_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_ccw = cv2.warpAffine(img, ccw_matrix, (w, h))

# Clockwise rotation (-45 degrees)
cw_matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated_cw = cv2.warpAffine(img, cw_matrix, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Counter Clockwise Rotation", rotated_ccw)
cv2.imshow("Clockwise Rotation", rotated_cw)

cv2.waitKey(0)
cv2.destroyAllWindows()
