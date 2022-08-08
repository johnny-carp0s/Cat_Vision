import torch
from matplotlib import pyplot as plt
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def cv_model(vid):
    yolo = model(vid)
    results = np.squeeze(yolo.render())
    
    return results