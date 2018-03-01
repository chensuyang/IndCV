#encoding=utf-8
import cv2
import sys
import numpy as np
import pprint 
import Image
import Camera
import ImageProcessing
import ContoursProcessing 
if __name__ == '__main__':
    MyCamera=Camera.Camera()
    MyCamera.open()
    MyCamera.set_framesize(Camera.Camera.VGA)
    mob_img=Image.Image(cv2.imread("C:\mob.jpg"))
    mob_img_data=mob_img.get_image_data()
    w= mob_img.get_image_width()
    h= mob_img.get_image_height()
    mob_img.change_color(cv2.COLOR_BGR2GRAY)
    
    while(1):
        img_data=MyCamera.snapshot()
        img = Image.Image(img_data)
        img.change_color(cv2.COLOR_BGR2GRAY)
        img_gray_data=img.get_image_data()
        mob_img_data=mob_img.get_image_data()
        res=cv2.matchTemplate(img_gray_data,mob_img_data,cv2.TM_CCOEFF_NORMED)
        threshold=0.6
        loc=np.where(res>=threshold)
        tmp_img_data= img.get_image_data()
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img=tmp_img_data,pt1=pt,pt2=(pt[0]+w,pt[1]+h),color=(7,249,151),lineType=8)
        cv2.imshow('trans1',loc)
        cv2.waitKey(10)
    sys.exit()
