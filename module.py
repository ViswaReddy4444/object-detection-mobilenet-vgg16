# to keep all the code here

import cv2
from ultralytics import YOLO
import tensorflow
from tensorflow import keras
from keras.applications import ResNet50,MobileNetV2,VGG16
import numpy as np


class project:

    def __init__(self,video_path,obj_det_path,img_cls_path):
        self.video_path = video_path
        self.obj_det_path = obj_det_path
        self.img_cls_path = img_cls_path

    def load_models(self):
        cls_model = keras.models.load_model(self.img_cls_path)
        obj_model = YOLO(self.obj_det_path)
        return cls_model,obj_model

    def process_video(self):

        source = cv2.VideoCapture(self.video_path)
        cls_model,obj_model = self.load_models()
        while True:
            ret,frame = source.read()
            if ret:
                results = obj_model.predict(frame,classes=16,verbose=False)
                if len(results[0]) >=1:
                    coordinates = results[0].boxes.xyxy.numpy()
                    for coord in coordinates:
                        x1 = int(coord[0])
                        y1 = int(coord[1])
                        x2 = int(coord[2])
                        y2 = int(coord[3])
                        cropped_image = frame[y1:y2,x1:x2]
                        resized_image = cv2.resize(cropped_image,(224,224))
                        resized_image = np.array([resized_image])  # Convert single image to a batch.
                        predictions = cls_model.predict(resized_image)
                        class_name = np.argmax(predictions,axis=1)
                        if class_name == 234:
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
                            # Trigger the action here 
                        elif class_name == 235:
                            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
                        
                        # cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
                cv2.imshow("window",frame)
                if cv2.waitKey(30) & 0xff == ord('q'):
                    break
            else:
                break
        source.release()
        cv2.destroyAllWindows()
        print(set(classes_index))