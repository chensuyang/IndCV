# -*- coding:UTF-8 -*-
import cv2
import numpy as np

class Image(object):
    "图像类,为每个图像数据的实例"
    RGB = cv2.COLOR_BGR2RGB
    BGR = cv2.COLOR_RGB2BGR
    GRAY = cv2.COLOR_BGR2GRAY
    HSV = cv2.COLOR_BGR2HSV
    LAB = cv2.COLOR_BGR2LAB
    def __init__(self, img_data=None, color_spaces=BGR):#类实例初始化
        self.image_data = img_data#图像数据
        self.image_color_spaces = color_spaces

    def get_image_data(self):
        """获取图像数据
        本方法会返回一个图像的numpy数组"""
        return self.image_data

    def set_image_data(self, img ,color_spaces=None):
        """设置图像数据
        img为图像的numpy数组
        成功返回True,失败返回False"""
        try:
            self.image_data = img
            if color_spaces:
                self.set_image_color_spaces(color_spaces)
                print("OK")
            return True
        except():
            return False
    
    def get_image_color_spaces(self):
        "获取图像颜色空间"
        return self.image_color_spaces

    def set_image_color_spaces(self,color_space):
        "设置图像颜色空间"
        if color_space == self.RGB:
            if self.get_image_color_spaces() == self.BGR:
                if self.change_color(cv2.COLOR_BGR2RGB):
                    self.image_color_spaces = self.RGB
                    return True
                return False
            elif self.get_image_color_spaces() == self.GRAY:
                if self.change_color(cv2.COLOR_GRAY2RGB):
                    self.image_color_spaces = self.RGB
                    return True
                return False
            elif self.get_image_color_spaces() == self.HSV:
                if self.change_color(cv2.COLOR_HSV2RGB):
                    self.image_color_spaces = self.RGB
                    return True
                return False
            elif self.get_image_color_spaces() == self.LAB:
                if self.change_color(cv2.COLOR_LAB2RGB):
                    self.image_color_spaces = self.RGB
                    return True
                return False
        elif color_space == self.BGR:
            if self.get_image_color_spaces() == self.RGB:
                if self.change_color(cv2.COLOR_RGB2BGR):
                    self.image_color_spaces = self.BGR
                    return True
                return False
            elif self.get_image_color_spaces() == self.GRAY:
                if self.change_color(cv2.COLOR_GRAY2BGR):
                    self.image_color_spaces = self.BGR
                    return True
                return False
            elif self.get_image_color_spaces() == self.HSV:
                if self.change_color(cv2.COLOR_HSV2BGR):
                    self.image_color_spaces = self.BGR
                    return True
                return False
            elif self.get_image_color_spaces() == self.LAB:
                if self.change_color(cv2.COLOR_LAB2BGR):
                    self.image_color_spaces = self.BGR
                    return True
                return False
        elif color_space == self.GRAY:
            if self.get_image_color_spaces() == self.RGB:
                if self.change_color(cv2.COLOR_RGB2GRAY):
                    self.image_color_spaces = self.GRAY
                    return True
                return False
            elif self.get_image_color_spaces() == self.BGR:
                if self.change_color(cv2.COLOR_BGR2GRAY):
                    self.image_color_spaces = self.GRAY
                    return True
                return False
        elif color_space == self.HSV:
            if self.get_image_color_spaces() == self.RGB:
                if self.change_color(cv2.COLOR_RGB2HSV):
                    self.image_color_spaces = self.HSV
                    return True
                return False
            elif self.get_image_color_spaces() == self.BGR:
                if self.change_color(cv2.COLOR_BGR2HSV):
                    self.image_color_spaces = self.HSV
                    return True
                return False
        elif color_space == self.LAB:
            if self.get_image_color_spaces() == self.RGB:
                if self.change_color(cv2.COLOR_RGB2LAB):
                    self.image_color_spaces = self.LAB
                    return True
                return False
            elif self.get_image_color_spaces() == self.BGR:
                if self.change_color(cv2.COLOR_BGR2LAB):
                    self.image_color_spaces = self.LAB
                    return True
                return False       
        return False
            

    def new_image_data(self, img_size, color):
        """创建新的图像数据
        img_size为一个2成员的tuple(图像宽,图像高)
        color为一个3成员的tuple"""
        try:
            image_data_tmp = np.zeros((img_size[1], img_size[0], 3), dtype=np.uint8)
            cv2.rectangle(image_data_tmp, (0, 0), (self.get_image_width(), self.get_image_height()), color, -1)#-1表示实心
            self.set_image_data(image_data_tmp)
            return True
        except():
            return False

    def get_image_height(self):
        """获取图像高度
        成功返回图像高度像素值,失败返回-1"""
        try:
            return self.image_data.shape[0]
        except():
            return -1

    def get_image_width(self):
        """获取图像宽度
        成功返回图像宽度像素值,失败返回-1"""
        try:
            return self.image_data.shape[1]
        except():
            return -1

    def change_color(self, flag):
        """转换颜色空间
        flag为转换方式,例如:cv2.COLOR_BGR2GRAY
        转换成功返回True,失败返回False"""
        try:
            image_data_tmp = np.zeros(self.image_data.shape, dtype=np.uint8)
            image_data_tmp = cv2.cvtColor(self.image_data, flag)#转换颜色空间
            self.image_data = image_data_tmp #替换图像数据
            return True
        except():
            return False

    def line(self, point1, point2, color=(0, 0, 255), thickness=1):
        """画直线
        point1为起点坐标,为一个2成员的tuple(X,Y)
        point2为终点坐标,为一个2成员的tuple(X,Y)
        color为线条颜色,为一个3成员的tuple
        thickness为线条像素宽度,为int
        成功返回True,失败返回False"""
        try:
            cv2.line(self.image_data, point1, point2, color, thickness)
            return True
        except():
            return False

    def rectangle(self, point1, point2, color=(0, 0, 255), thickness=1):
        """画矩形
        point1为左上角坐标,为一个2成员的tuple(X,Y)
        point2为右下角坐标,为一个2成员的tuple(X,Y)
        color为线条颜色,为一个3成员的tuple
        thickness为线条像素宽度(-1为实心),为int
        成功返回True,失败返回False"""
        try:
            cv2.rectangle(self.image_data, point1, point2, color, thickness)
            return True
        except():
            return False

    def circle(self, center_point, radius, color=(0, 0, 255), thickness=1):
        """画圆
        center_point为圆心坐标,为一个2成员的tuple(X,Y)
        radius为半径的像素值
        color为线条颜色,为一个3成员的tuple
        thickness为线条像素宽度(-1为实心),为int
        成功返回True,失败返回False"""
        try:
            cv2.circle(self.image_data, center_point, radius, color, thickness)
            return True
        except():
            return False
 
    def text(self, text_string, org, font=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2):
        """写文本
        text_string为要写入的文本,为string
        org为文本开始的左下角坐标,为2成员的tuple(X,Y)
        font为字体类型,例如cv2.FONT_HERSHEY_SIMPLEX
        fontScale为字体缩放因子,为int
        color为字体颜色,为一个3成员的tuple
        thickness为字体厚度,为int"""
        try:
            cv2.putText(self.image_data, text_string, org, font, fontScale, color, thickness)
            return True
        except():
            return False
    
    def cross(self, point, cross_len, color=(0, 0, 255), thickness=1):
        """画十字
        point为十字中心点,为2成员的tuple(X,Y)
        len为十字线(水平线与垂直线)半长,为int
        color为线条颜色,为一个3成员的tuple
        thickness为线条厚度,为int"""
        try:
            self.line((point[0]-cross_len, point[1]), (point[0]+cross_len, point[1]), color, thickness)
            self.line((point[0], point[1]-cross_len), (point[0], point[1]+cross_len), color, thickness)
            return True
        except():
            return False
    
    def bitwise_not(self):
        """将本图像求反(即白变黑)"""
        try:
            self.set_image_data(cv2.bitwise_not(self.get_image_data()))
            return True
        except():
            return False
    
    def bitwise_and(self, img_obj, mask=None):
        """将本图像与另一幅图像求和
        img_obj为另一幅与本图像求和的图像
        mask为掩膜,不需要时可为None
        """
        try:
            self.set_image_data(cv2.bitwise_and(self.get_image_data(), img_obj.get_image_data(), mask))
            return True
        except():
            return False

    def bitwise_or(self, img_obj, mask=None):
        "将本图像与另一幅图像或运算"
        try:
            self.set_image_data(cv2.bitwise_or(self.get_image_data(), img_obj.get_image_data(), mask))
            return True
        except():
            return False

    def bitwise_xor(self, img_obj, mask=None):
        "将本图像与另一幅图像异或运算"
        try:
            self.set_image_data(cv2.bitwise_xor(self.get_image_data(), img_obj.get_image_data(), mask))
            return True
        except():
            return False

    def split(self):
        """将本图像的三个通道分离为三个图像"""
        try:
            b,g,r = cv2.split(self.image_data)
            img1 = Image(b, self.GRAY)
            img2 = Image(g, self.GRAY)
            img3 = Image(r, self.GRAY)
            return img1,img2,img3
        except():
            return False
