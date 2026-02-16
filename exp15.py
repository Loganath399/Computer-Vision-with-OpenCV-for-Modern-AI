import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\logan\OneDrive\Desktop\exp2.png")

if img is None:
    print("Error: Image not found")
    exit()

rows, cols = img.shape[:2]

# Source points (minimum 4)
src_pts = np.array([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
], dtype=np.float32)

# Destination points
dst_pts = np.array([
    [30, 100],
    [280, 50],
    [80, 300],
    [320, 280]
], dtype=np.float32)

# ---------------- DLT IMPLEMENTATION ----------------
A = []

for i in range(4):
    x, y = src_pts[i]
    xp, yp = dst_pts[i]

    A.append([-x, -y, -1, 0, 0, 0, x*xp, y*xp, xp])
    A.append([0, 0, 0, -x, -y, -1, x*yp, y*yp, yp])

A = np.array(A)

# Solve Ah = 0 using SVD
U, S, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)

# Normalize homography matrix
H = H / H[2, 2]

# Apply transformation
dlt_img = cv2.warpPerspective(img, H, (cols, rows))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", dlt_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
