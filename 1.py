#encoding=utf-8
import cv2
import sys
import numpy as np
import pprint 
import Image
import Camera
import ImageProcessing
import ContoursProcessing 
import AprilTagsLib

if __name__ == '__main__':
    MyCamera=Camera.Camera()
    MyCamera.open()
    MyCamera.set_framesize(Camera.Camera.VGA)    
    while(1):
	img_data=MyCamera.snapshot()
        img = Image.Image(img_data)
    	img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        img3=AprilTagsLib.Mat.from_array(img2)
        str=AprilTagsLib.extractTags(4,img3)
	    pprint.pprint(str)
        cv2.waitKey(10)
    sys.exit()
