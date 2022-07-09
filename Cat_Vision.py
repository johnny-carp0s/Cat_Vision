import cv2 as cv
import Cat_Detection as cd

garagem_ext = 1
fundos_esq = 2
fundos_dir = 3
tangara = 4
garagem_int = 5
servico = 6

channel = fundos_esq
cam = f'rtsp://admin:%2C06YtO%2Fj@192.168.0.151:554/cam/realmonitor?channel={channel}&subtype=0'

cap = cv.VideoCapture(cam)

while(cap.isOpened()):
    ret, frame = cap.read()

    #detections
    results = cd.cv_model(frame)

    cv.imshow("Frame", results)

    key = cv.waitKey(10)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()