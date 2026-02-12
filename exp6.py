import cv2

video_path = r"C:\Users\logan\OneDrive\Desktop\sample_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

print("Press q to quit")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Normal speed
    cv2.imshow("Normal Speed", frame)
    cv2.waitKey(30)

    # Slow motion
    cv2.imshow("Slow Motion", frame)
    cv2.waitKey(120)

    # Fast motion
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
