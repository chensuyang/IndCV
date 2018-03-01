# -*- coding:UTF-8 -*-
import cv2
import numpy as np
import Image
class ImageProcessing(object):
    "图像处理类,包含了常用的图像处理算法"

    @staticmethod
    def resize(img_obj, width, height):
        """对本图像进行缩放
        img_obj为输入的图像
        width为缩放后的图像宽度
        height为缩放后的图像高度"""
        try:
            img_obj.set_image_data(cv2.resize(img_obj.get_image_data(), ( int(width), int(height)), interpolation=cv2.INTER_AREA))
            return True
        except():
            return False

    @staticmethod    
    def warpAffine(img_obj, src_tri, dst_tri):
        """设定本图像的三点位置以及变换结束后该三点所在的位置来进行仿射变换
        img_obj为输入的图像
        src_tri为原图像三点的位置,为一个有3个list(每个list内为两个int)成员的list
        src_tri为变换后原图像三点的位置,为一个有3个list(每个list内为两个int)成员的list
        """
        try:
            pts1 = np.float32(src_tri)
            pts2 = np.float32(dst_tri)
            warp = cv2.getAffineTransform(pts1, pts2)
            img_data_tmp = img_obj.get_image_data()
            img_obj.set_image_data(cv2.warpAffine(img_data_tmp, warp, (img_obj.get_image_width(),img_obj.get_image_width())))
            return True
        except():
            return False

    @staticmethod    
    def warpPerspective(img_obj, src_tri, dst_tri):
        """设定本图像的四点位置以及透射结束后该四点所在的位置来进行透射变换
        img_obj为输入的图像
        src_tri为原图像四点的位置,为一个有4个list(每个list内为两个int)成员的list
        src_tri为变换后原图像四点的位置,为一个有4个list(每个list内为两个int)成员的list
        """
        try:
            pts1 = np.float32(src_tri)
            pts2 = np.float32(dst_tri)
            warp = cv2.getPerspectiveTransform(pts1, pts2)
            img_data_tmp = img_obj.get_image_data()
            img_obj.set_image_data(cv2.warpPerspective(img_data_tmp, warp, (img_obj.get_image_width(), img_obj.get_image_width())))
            return True
        except():
            return False

    @staticmethod
    def GaussianBlur(img_obj, kernel_width):
        """将图像进行高斯模糊处理
        img_obj为输入的图像
        kernel_width为内核宽高度(为奇数,若输入双数则自动+1)
        """
        try:
            if kernel_width%2 == 0:
                kernel_width_tmp = kernel_width+1
            else:
                kernel_width_tmp = kernel_width
            img_obj.set_image_data(cv2.GaussianBlur(img_obj.get_image_data(), (kernel_width_tmp, kernel_width_tmp), 0))
            return True
        except():
            return False
    
    @staticmethod
    def medianBlur(img_obj, kernel_width):
        """将图像进行中位数模糊,对于去除图像中的椒盐噪音非常有效
        img_obj为输入的图像
        kernel_width为内核宽高度(为奇数,若输入双数则自动+1)
        """
        try:
            if kernel_width%2 == 0:
                kernel_width_tmp = kernel_width+1
            else:
                kernel_width_tmp = kernel_width
            img_obj.set_image_data(cv2.medianBlur(img_obj.get_image_data(), kernel_width_tmp))
            return True
        except():
            return False

    @staticmethod
    def bilateralFilter(img_obj, d=9, sigma_color=75, sigma_space=75):
        """将图像进行双边过滤,消除噪音方面非常有效，同时保持边缘清晰
        img_obj为输入的图像
        kernel_width为内核宽高度(为奇数,若输入双数则自动+1)
        """
        try:
            img_obj.set_image_data(cv2.bilateralFilter(img_obj.get_image_data(), d, sigma_color, sigma_space))
            return True
        except():
            return False

    @staticmethod
    def threshold(img_obj, thresh):
        """固定阀值二值化,通过一个固定的阀值将图像进行黑白二值化
        img_obj为输入的图像
        thresh为阀值"""
        try:
            if img_obj.get_image_color_spaces() != Image.Image.GRAY:
                img_obj.set_image_color_spaces(Image.Image.GRAY)
            img_data_tmp = img_obj.get_image_data()
            ret, img_data_tmp = cv2.threshold(img_data_tmp, thresh, 255, cv2.THRESH_BINARY)
            img_obj.set_image_data(img_data_tmp)
            return True
        except():
            return False

    @staticmethod
    def adaptiveThreshold(img_obj):
        """自适应阀值二值化,通过将图像分割为数个小区域,在小区域生成对应的区域阀值来将图像进行黑白二值化
        img_obj为输入的图像"""
        try:
            if img_obj.get_image_color_spaces() != Image.Image.GRAY:
                img_obj.set_image_color_spaces(Image.Image.GRAY)
            img_data_tmp = img_obj.get_image_data()
            img_obj.set_image_data(cv2.adaptiveThreshold(img_data_tmp ,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2))
            return True
        except():
            return False

    @staticmethod
    def threshold_otsu(img_obj):
        """自动取优阀值二值化
        img_obj为输入的图像"""
        try:
            if img_obj.get_image_color_spaces() != Image.Image.GRAY:
                img_obj.set_image_color_spaces(Image.Image.GRAY)
            img_data_tmp = img_obj.get_image_data()
            img_data_tmp = cv2.GaussianBlur(img_data_tmp, (5, 5), 0)
            ret3, img_data_tmp = cv2.threshold(img_data_tmp, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            img_obj.set_image_data(img_data_tmp)
            return True
        except():
            return False

    @staticmethod
    def Canny(img_obj, threshold_min_val, threshold_max_val):
        """Canny边缘检测
        img_obj为输入的图像
        threshold_min_val最低阀值,低于此值的边缘无条件丢弃
        threshold_max_val最高阀值,高于此值的边缘无条件保留"""
        try:
            if img_obj.get_image_color_spaces() != Image.Image.GRAY:
                img_obj.set_image_color_spaces(Image.Image.GRAY)
            img_data_tmp = img_obj.get_image_data()
            img_data_tmp = cv2.GaussianBlur(img_data_tmp, (5, 5), 0)
            img_obj.set_image_data(cv2.Canny(img_data_tmp, threshold_min_val, threshold_max_val))
            return True
        except():
            return False

    @staticmethod
    def erode(img_obj, kernel_width):
        """将图像进行侵蚀处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.erode(img_obj.get_image_data(), kernel, iterations = 1))
            return True
        except():
            return False

    @staticmethod
    def dilate(img_obj, kernel_width):
        """将图像进行扩张处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.dilate(img_obj.get_image_data(), kernel, iterations = 1))
            return True
        except():
            return False
        
    @staticmethod
    def Opening(img_obj, kernel_width):
        """将图像进行打开处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.morphologyEx(img_obj.get_image_data(), cv2.MORPH_OPEN, kernel))
            return True
        except():
            return False

    @staticmethod
    def Closing(img_obj, kernel_width):
        """将图像进行关闭处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.morphologyEx(img_obj.get_image_data(), cv2.MORPH_CLOSE, kernel))
            return True
        except():
            return False

    @staticmethod
    def Morphological_Gradient(img_obj, kernel_width):
        """将图像进行形态渐变处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.morphologyEx(img_obj.get_image_data(), cv2.MORPH_GRADIENT, kernel))
            return True
        except():
            return False
        

    @staticmethod
    def Top_Hat(img_obj, kernel_width):
        """将图像进行顶帽处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.morphologyEx(img_obj.get_image_data(), cv2.MORPH_TOPHAT, kernel))
            return True
        except():
            return False

    @staticmethod
    def Black_Hat(img_obj, kernel_width):
        """将图像进行黑帽处理
        img_obj为输入的图像
        kernel_width为内核宽高度"""
        try:
            kernel = np.ones((kernel_width, kernel_width), np.uint8)
            img_obj.set_image_data(cv2.morphologyEx(img_obj.get_image_data(), cv2.MORPH_BLACKHAT, kernel))
            return True
        except():
            return False
        