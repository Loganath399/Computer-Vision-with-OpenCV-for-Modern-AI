import cv2

# Step 1: Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to quit")

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Normal display (reference)
    cv2.imshow("Normal Webcam Video", frame)

    # Slow motion (repeat same frame with delay)
    cv2.imshow("Slow Motion Webcam Video", frame)
    cv2.waitKey(120)   # higher delay → slow motion

    # Fast motion (skip frames)
    if frame_count % 3 == 0:   # show every 3rd frame
        cv2.imshow("Fast Motion Webcam Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
