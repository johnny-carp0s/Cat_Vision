import cv2 as cv
import Cat_Detection as cd
import threading

#Valor cameras
garagem_ext = 1
fundos_esq = 2
fundos_dir = 3
tangara = 4
garagem_int = 5
servico = 6

#função para fonte de cameras pelo link da intelbras
def captura_cam(cam):
        camera = f'rtsp://admin:%2C06YtO%2Fj@192.168.0.151:554/cam/realmonitor?channel={cam}&subtype=0'
        return camera

#Captura dos videos das cameras TESTE
cap_gararem_ext = cv.VideoCapture(captura_cam(garagem))
cap_fundos_esq = cv.VideoCapture(cam)
cap_ = cv.VideoCapture(cam)
cap = cv.VideoCapture(cam)
cap = cv.VideoCapture(cam)
cap = cv.VideoCapture(cam)

#altura e largura dos videos para salvar
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

print(frame_width)
print(frame_height)

size = (frame_width, frame_height)

#Check para salvar o video e nomear arquivo
file_name = ""
save = input("Do you want to save this video? (y/n)")
if(save == "y"):
    file_name = input("What's the file name? ")
    result = cv.VideoWriter(f"Saved Videos/{file_name}.avi", cv.VideoWriter_fourcc(*'MP4V'), 10, size)

#Check se video esta funcionando
if (cap.isOpened() == False):
	print("Error reading video file")

#PROCESSAMENTO DO VIDEO
while(cap.isOpened()):

    #leitura de frame
    ret, frame = cap.read()

    #Detecção de objetos no frame do video
    results, cat = cd.cv_model(frame)

    #Salva frame do video
    if(save == "y"):
        result.write(results)

    #Ações se encontrar gato
    if cat:
        cv.putText(img=results, org=(100,250), text="GATO ENCONTRADO!!!",
            fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=3)

    #Display de video
    cv.imshow("Frame", results)

    #Controle do display do video
    key = cv.waitKey(10)
    if key == 27:
        break

#Finaliza captura e video
cap.release()
cv.destroyAllWindows()