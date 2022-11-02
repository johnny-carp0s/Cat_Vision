import cv2 as cv
import Cat_Detection as cd
import threading
from time import sleep
import os

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
    def __init__(self, previewName, camID, frame=0, cat=False, rval=True):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.cat = cat
        self.frame = frame
        self.rval = rval
    def run(self):
        print ("Starting " + self.previewName)
        camProcessing(self)

def camProcessing(cm):

    #cv.namedWindow(cm.previewName)
    cam = cv.VideoCapture(cm.camID)
    if cam.isOpened():  # try to get the first frame
        cm.rval, cm.frame = cam.read()
    else:
        print(f"Error reading {cm.previewName} video file")
        cm.rval = False

    #PROCESSAMENTO DO VIDEO
    while cm.rval:
        #cv.imshow(cm.previewName, cm.frame)
        cm.rval, cm.frame = cam.read()

        #Detecção de objetos no frame do video
        results, cm.cat = cd.cv_model(cm.frame)   

        key = cv.waitKey(20)
        if key == 27:  # exit on ESC
            cm.rval = False
            break
    cv.destroyWindow(cm.previewName)


def gato_encontrado():
    #Valor gato encontrado
    gato_i = len(os.listdir("Gatos2"))+1

    array_g = [thread_g_ext, thread_f_esq, thread_f_dir, thread_tanga, thread_g_int, thread_servi]

    while thread_g_ext.rval == True:
        for g in array_g:
            if g.cat == True:
                gato_loc = f'Gatos2/gato{gato_i}.png'
                cv.imwrite(gato_loc, g.frame)
                cd.save_to_db(gato_loc, g.previewName)
                gato_i = gato_i + 1
        
        sleep(2)

check_gatos = threading.Thread(target=gato_encontrado)

#"object_tracking/Branco-Tangara.mp4"
thread_g_ext = camThread("garagem_ext", captura_cam(garagem_ext)) #
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
check_gatos.start()