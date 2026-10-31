import cv2
from processing import processing

#get video from the first device on the computer
cap = cv2.VideoCapture(0)

processor = processing()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Waiting for stream packet...")
        continue

    processedImage = processor.processFrame(frame)
    cv2.imshow("Processed Image", processedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'): #waitKey(1) allows for continous feed of images, press q to quit
        break

cap.release()
cv2.destroyAllWindows()
