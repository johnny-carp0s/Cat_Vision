import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img = 'images.jpg'

results = model(img)
results.print()
results.show()

# cv.imshow("resukts", results.render())
# cv.waitKey(0)
# cv.destroyAllWindows()