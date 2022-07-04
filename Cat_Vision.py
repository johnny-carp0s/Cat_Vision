import cv2 as cv

garagem_ext = 1
fundos_esq = 2
fundos_dir = 3
tangara = 4
garagem_int = 5
servico = 6

channel = tangara
cam = f'rtsp://admin:%2C06YtO%2Fj@192.168.0.151:554/cam/realmonitor?channel={channel}&subtype=0'

cap = cv.VideoCapture(cam)

while(True):
    ret, frame = cap.read()

    cv.imshow("Frame", frame)

    key = cv.waitKey(30)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()