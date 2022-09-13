import torch
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import os

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

def save_to_db(img, camera):
    df = pd.read_excel(db, engine="openpyxl")
    writer = pd.ExcelWriter(db, engine="xlsxwriter")

    #pegar data
    agora = datetime.now()
    dt_string = agora.strftime("%d/%m/%Y %H:%M:%S")

    #dataframe que vai ser adicionado
    df_new = pd.DataFrame({"Data":[dt_string], "Camera":[camera]})

    #juntar e salvar
    df = pd.concat([df, df_new], ignore_index=True)
    print(df)
    df.to_excel(writer, index=False)

    #adicionar imagem
    worksheet = writer.sheets["Sheet1"]
    i = 2

    #add previous images
    for cat in os.listdir("Gatos"):
        worksheet.insert_image(f'A{i}', f"Gatos/{cat}", {'x_scale': 0.1, 'y_scale': 0.1, 'object_position': 2})
        worksheet.set_row(i-1, 85)
        i = i+1
    
    rows_count = len(df.index)
    worksheet.insert_image(f'A{rows_count+1}', img, {'x_scale': 0.1, 'y_scale': 0.1, 'object_position': 2})
    worksheet.set_row(rows_count, 85)
    worksheet.set_column(1, 1, 20)
    worksheet.set_column(0, 0, 27)
    print("image inserted")

    writer.save()