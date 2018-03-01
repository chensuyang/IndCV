# -*- coding:UTF-8 -*-
import cv2

class Camera(object):
    "摄像头类,通过本类来设置摄像头参数并获取摄像头图像"
    UVGA = 1280960
    XGA = 1024768
    SVGA = 800600
    VGA = 640480
    QVGA = 320240

    def set_framesize(self, camera_frame_size):#设置分辨率
        "设置摄像头图像分辨率"
        if camera_frame_size == self.QVGA:#设置画面分辨率
            self.frame_width = 320
            self.frame_height = 240
            if self.cap.isOpened():#判断摄像头有没有打开
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)#设置画面宽度
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)#设置画面高度
                return self.QVGA
        elif camera_frame_size == self.VGA:
            self.frame_width = 640
            self.frame_height = 320
            if self.cap.isOpened():#判断摄像头有没有打开
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)#设置画面宽度
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)#设置画面高度
                return self.VGA
        elif camera_frame_size == self.SVGA:
            self.frame_width = 800
            self.frame_height = 600
            if self.cap.isOpened():#判断摄像头有没有打开
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)#设置画面宽度
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)#设置画面高度
                return self.SVGA
        elif camera_frame_size == self.XGA:
            self.frame_width = 1024
            self.frame_height = 768
            if self.cap.isOpened():#判断摄像头有没有打开
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)#设置画面宽度
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)#设置画面高度
                return self.XGA
        elif camera_frame_size == self.UVGA:
            self.frame_width = 1280
            self.frame_height = 960
            if self.cap.isOpened():#判断摄像头有没有打开
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)#设置画面宽度
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)#设置画面高度
                return self.UVGA
        else:
            return -1#找不到对应的分辨率


    def __init__(self):#类实例初始化
        self.frame_width = 640
        self.frame_height = 480
        self.cap = None


    def open(self, camera_index=0):
        "打开摄像头"
        self.cap = cv2.VideoCapture(camera_index)#创建VideoCapture类实例


    def snapshot(self):
        "用已经打开的摄像头获取一张图像"
        success, frame = self.cap.read()#获取一张图像
        if success:
            return frame
        return None


    def release(self):
        "卸载摄像头"
        self.cap.release()
