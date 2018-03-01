# -*- coding:UTF-8 -*-
import cv2
import numpy as np
import Image


def MatchTemplate(img_obj,template_obj,method,threshold):
    try:
        if img_obj.get_image_color_spaces() != Image.Image.GRAY:#这边是确保图像为GRAY
            img_obj.set_image_color_spaces(Image.Image.GRAY)
        img_data_tmp = img_obj.get_image_data()
        if template_obj.get_image_color_spaces() != Image.Image.GRAY:#这边是确保图像为GRAY
            template_obj.set_image_color_spaces(Image.Image.GRAY)
        mob_data_tmp = template_obj.get_image_data()
        res=cv2.matchTemplate(img_data_tmp,mob_data_tmp,method)#模板匹配
        loc=np.where(res>=threshold)#对比匹配结果,筛出匹配结果图像中值大于等于threshold的坐标
        tmp_img_data= img_obj.get_image_data()
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img=tmp_img_data,pt1=pt,pt2=(pt[0]+w,pt[1]+h),color=(7,249,151),lineType=8)

