import cv2

# images
img = cv2.imread("C:/Users/arthu/Pictures/Saved Pictures/109676.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

'''# videos
cap = cv2.VideoCapture("directory/filename")

while True:
    sucess, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# webcam
cap = cv2.VideoCapture(0)
resolution(cap, 640, 480, 100)

while True:
    sucess, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''