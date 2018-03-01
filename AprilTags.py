# -*- coding:UTF-8 -*-
import cv2
import numpy as np
import  AprilTagsLib.AprilTagsLib
import Image



def  extractTags(AprilTag_code,img_obj):
    """finding Tags"""
    try:
        if img_obj.get_image_color_spaces() != Image.Image.GRAY:
            img_obj.set_image_color_spaces(Image.Image.GRAY)
        img_data_tmp = img_obj.get_image_data()
        img=AprilTagsLib.AprilTagsLib.Mat.from_array(img_data_tmp)
        tags_str_info=AprilTagsLib.AprilTagsLib.extractTags(AprilTag_code,img)
        tags_str_info_list=tags_str_info.split("\n")
        for index in range(len(tags_str_info_list)):
            tag_info_list=tags_str_info_list[index].split("|")
            tag_info_dict={}
            tag_info_dict['Id']=tag_info_list[0]
            tag_info_dict['X']=tag_info_list[1]
            tag_info_dict['Y']=tag_info_list[2]
            tag_info_dict['XYOrientation']=tag_info_list[3]
            tag_info_dict['Distance']=tag_info_list[4]
            tag_info_dict['XM']=tag_info_list[5]
            tag_info_dict['YM']=tag_info_list[6]
            tag_info_dict['ZM']=tag_info_list[7]
            tag_info_dict['Yaw']=tag_info_list[8]
            tag_info_dict['Pitch']=tag_info_list[9]
            tag_info_dict['Roll']=tag_info_list[10]
            tag_info_list.append(tag_info_dict)
            return tag_info_list
    except():
        return None
    
