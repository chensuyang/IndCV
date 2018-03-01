# -*- coding:UTF-8 -*-
import cv2
import numpy as np
import Image
import ImageProcessing
import pprint  
class ContoursProcessing(object):
    "轮廓处理类,包含了常用的轮廓相关的处理算法"

    @staticmethod
    def findContours(img_obj):
        """在图像中寻找轮廓
        img_obj为输入的图像
        返回contours, hierarchy"""
        try:
            if img_obj.get_image_color_spaces() != Image.Image.GRAY:
                img_obj.set_image_color_spaces(Image.Image.GRAY)
            img_data_tmp = img_obj.get_image_data()
            img, contours, hierarchy = cv2.findContours(img_data_tmp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#寻找边缘
            """img_obj.set_image_color_spaces(Image.Image.BGR)
            for i in range(0,len(contours)):
                contour=contours[i]
                for j in range(0,len(contour)-1):
                    #print("pos:%d,%d \r\n"%(int(i[j][0][0]),int(i[j][0][1])))
                    img_obj.line((int(contour[j][0][0]),int(contour[j][0][1])),(int(contour[j+1][0][0]),int(contour[j+1][0][1])))
                img_obj.line((int(contour[len(contour)-1][0][0]),int(contour[len(contour)-1][0][1])),(int(contour[0][0][0]),int(contour[0][0][1])))
                img_obj.text(str(i),(int(contour[0][0][0]),int(contour[0][0][1])))
            pprint.pprint(hierarchy)"""
            return contours, hierarchy
            return True
        except():
            return False