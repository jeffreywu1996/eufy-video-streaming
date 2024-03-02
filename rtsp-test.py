import cv2
cap = cv2.VideoCapture("rtsp://Ff3Dl5Al9hlc:Qy8gcQtDBTXB@192.168.1.252/live0")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
