
# import the opencv library
import cv2 
import time
import os
# define a video capture object

# CV 
# !pip3 install transformers

from transformers import BeitFeatureExtractor, BeitForImageClassification
from PIL import Image
import requests

vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(2)
counter = 0
while(True):
    # Capture the video frame
    # by frame
    ret1, frame1 = vid1.read()
    ret2, frame2 = vid2.read()
    
    # Display the resulting frame
    
    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    # path = '/home/ale/Desktop/nDATASET/con_fondo_bolsa_banana'
    path = '/home/ale/Desktop/detection'
    
    # time.sleep(6)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        cv2.imwrite(os.path.join(path , 'detection'+str(counter)+'.png'),frame1)
        counter = counter + 1
        print("Toma foto..")
        
        image = Image.open('/home/ale/Desktop/detection/'++str(counter)+'.png')
        image = image.convert('RGB')
        
        feature_extractor = BeitFeatureExtractor.from_pretrained('microsoft/beit-large-patch16-512')
        model = BeitForImageClassification.from_pretrained('microsoft/beit-large-patch16-512')

        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        # model predicts one of the 1000 ImageNet classes
        predicted_class_idx = logits.argmax(-1).item()
        print("Predicted class:", model.config.id2label[predicted_class_idx])
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the cap object
vid1.release()
vid2.release()
# Destroy all the windows
cv2.destroyAllWindows()