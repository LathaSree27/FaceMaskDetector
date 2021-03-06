# -*- coding: utf-8 -*-
"""Sci IR Mask Testing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1326biMABaXgGXrzgPmvRVCBRVf2mwgyY

**importing the necessary packages**
"""

from google.colab.patches import cv2_imshow
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import cv2
from termcolor import colored
from tensorflow.keras.preprocessing.image import load_img
from imutils import paths

"""**Loading the Trained Model**"""

model_mv2 = load_model("/content/drive/MyDrive/Sci_Output/mv2Model.model")
model_incp = load_model("/content/drive/MyDrive/Sci_Output/InceptionModel.model")
model_vgg = load_model("/content/drive/MyDrive/Sci_Output/vggModel.model")

"""**Defining Required Functions**"""

#probability of Mask and No Mask
def prob(mask, withoutMask):
  label = "Mask" if mask > withoutMask else "No Mask"
  lab = "\033[1m"+"{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)+"\033[0m"
  if label=="Mask":
    lab=colored(lab,"green")
  else:
    lab=colored(lab,"red")
  return lab


def output_prediction(image):
  image=cv2.resize(image, (224, 224))
  processed_image = img_to_array(image)
  processed_image = preprocess_input(processed_image)
  processed_image = np.expand_dims(processed_image, axis=0)

  #displayinmg image
  cv2_imshow(image)

  #for mobilenet v2
  (mask, withoutMask)=model_mv2.predict(processed_image)[0]
  print("\nMobileNetV2: "+prob(mask, withoutMask))

  # for Inception
  (mask, withoutMask)=model_incp.predict(processed_image)[0]
  print("\nInceptionResNetv2: "+prob(mask, withoutMask)) 

  #for VGG
  (mask, withoutMask)=model_vgg.predict(processed_image)[0]
  print("\nVGG: "+prob(mask, withoutMask))

"""**Predicting class label for new image 1**"""

image=cv2.imread("/content/drive/MyDrive/10.jpg")
output_prediction(image)

"""**Predicting class label for new image 2**"""

image=cv2.imread("/content/drive/MyDrive/pred/2.jpg")
output_prediction(image)

"""**Predicting class label for new image 3**"""

image=cv2.imread("/content/drive/MyDrive/pred/500.png")
output_prediction(image)

image=cv2.imread("/content/drive/MyDrive/pred/4.jpg")
output_prediction(image)

image=cv2.imread("/content/drive/MyDrive/50.png")
output_prediction(image)

image=cv2.imread("/content/drive/MyDrive/61.jpg")
output_prediction(image)