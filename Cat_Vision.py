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

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print ("Starting " + self.previewName)
        camProcessing(self.previewName, self.camID)

def camProcessing(previewName, camID):
    cv.namedWindow(previewName)
    cam = cv.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()

        #altura e largura dos videos para salvar
        frame_width = int(cam.get(3))
        frame_height = int(cam.get(4))
        size = (frame_width, frame_height)
    else:
        print(f"Error reading {previewName} video file")
        rval = False

    #PROCESSAMENTO DO VIDEO
    while rval:
        cv.imshow(previewName, frame)
        rval, frame = cam.read()

        #Detecção de objetos no frame do video
        results, cat = cd.cv_model(frame)

        #Ações se encontrar gato
        if cat:
            cv.putText(img=results, org=(100,250), text="GATO ENCONTRADO!!!",
            fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=3)

        key = cv.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv.destroyWindow(previewName)

thread_g_ext = camThread("garagem_ext", captura_cam(garagem_ext))
thread_f_esq = camThread("fundos_esq", captura_cam(fundos_esq))
thread_f_dir = camThread("fundos_dir", captura_cam(fundos_dir))
thread_tanga = camThread("tangara", captura_cam(tangara))
thread_g_int = camThread("garagem_int", captura_cam(garagem_int))
thread_servi = camThread("servico", captura_cam(servico))

thread_g_ext.start()
thread_f_esq.start()
thread_f_dir.start()
thread_tanga.start()
thread_g_int.start()
thread_servi.start()



#Check para salvar o video e nomear arquivo
#file_name = ""
#save = input("Do you want to save this video? (y/n)")
#if(save == "y"):
#    file_name = input("What's the file name? ")
#    result = cv.VideoWriter(f"Saved Videos/{file_name}.avi", cv.VideoWriter_fourcc(*'MP4V'), 10, size)

#Salva frame do video
    #if(save == "y"):
        #result.write(results)