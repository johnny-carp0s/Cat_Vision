import torch
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#Import do modelo IA
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

#Processamento de imagem e detecção de objetos
def cv_model(vid):
    yolo = model(vid)
    results = np.squeeze(yolo.render())

    #Detecção de gato
    objects = pd.DataFrame(yolo.pandas().xyxy[0])
    cat = "dog" in objects["name"].values or "cat" in objects["name"].values
    
    return results, cat