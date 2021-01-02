import cv2 as cv

def reseolution(img, width, height, brightness):
    cap.set(3, width)
    cap.set(4, height)
    cap.set(10, brightness)


cap = cv.VideoCapture(0)
reseolution(cap, 1080, 720, 100)

haar_cascade = cv.CascadeClassifier('haar_face.xml')


while True:
    sucess, img = cap.read()
    gray_cap = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_react = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)
    print(len(faces_react))
    for (x, y, w, h) in faces_react:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow("Webcam", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break