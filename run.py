# to keep only what is required

from module import *
import warnings
warnings.filterwarnings("ignore") # i want to detect only rotwiller not german shepered


pipeline = project(video_path="source/dog.mp4",
                   obj_det_path = "weights/object_detection/yolov8n.pt",
                   img_cls_path="weights/image_classification/vgg16.keras")

pipeline.process_video()
                    



