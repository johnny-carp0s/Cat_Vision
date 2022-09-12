import torch
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

#Import do modelo IA
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

#start database
db = "Cat_Vision_db.xlsx"

#Processamento de imagem e detecção de objetos
def cv_model(vid):
    yolo = model(vid)
    results = np.squeeze(yolo.render())

    #Detecção de gato
    objects = pd.DataFrame(yolo.pandas().xyxy[0])
    cat = "dog" in objects["name"].values or "cat" in objects["name"].values
    
    return results, cat

def save_to_db(img, camera, index):
    df = pd.read_excel(db)
    writer = pd.ExcelWriter(db, engine="xlsxwriter")

    #pegar data
    agora = datetime.now()
    dt_string = agora.strftime("%d/%m/%Y %H:%M:%S")

    #dataframe que vai ser adicionado
    df_new = pd.DataFrame({ "data":[dt_string], "camera":[camera]})

    #adicionar imagem
    worksheet = writer.sheets["Sheet1"]
    worksheet.insert_image(f'C{index}', img, {'x_scale': 0.25, 'y_scale': 0.25})

    #juntar e salvar
    df = pd.concat([df, df_new], ignore_index=True)
    df.to_excel(writer, index=False)
    print(df)

    writer.save()