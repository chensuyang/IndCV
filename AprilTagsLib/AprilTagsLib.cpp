#include <iostream>
#include <vector>
#include <list>
#include <sys/time.h>
#include "TagDetector.h"
#include "Tag16h5.h"
#include "Tag25h7.h"
#include "Tag25h9.h"
#include "Tag36h9.h"
#include "Tag36h11.h"
#include "opencv2/core/core.hpp"
#include <string>
using namespace std;
#ifndef PI
const double PI = 3.14159265358979323846;
#endif
const double TWOPI = 2.0*PI;

/*AprilTag_code*/
#define APRIL_TAG_CODE_TAG16H5 0
#define APRIL_TAG_CODE_TAG25H7 1
#define APRIL_TAG_CODE_TAG25H9 2
#define APRIL_TAG_CODE_TAG36H9 3
#define APRIL_TAG_CODE_TAG36H11 4

int m_width=640; // image size in pixels
int m_height=480;
double m_tagSize=0.05; // April tag side length in meters of square black frame
double m_fx=2.97/3*m_width; //x的像素为单位的焦距，应该等于2.97/3*1952，这个值是用毫米为单位的焦距除以x方向的感光元件的长度，乘以x方向的感光元件的像素（OV2710）
double m_fy=2.97/3*m_height; //y的像素为单位的焦距，应该等于2.97/3*1092，这个值是用毫米为单位的焦距除以y方向的感光元件的长度，乘以y方向的感光元件的像素（OV2710）
double m_px=m_width/2; //图像的x中心位置
double m_py=m_height/2; //图像的y中心位置

inline double standardRad(double t) 
{
  if (t >= 0.) {
    t = fmod(t+PI, TWOPI) - PI;
  } else {
    t = fmod(t-PI, -TWOPI) + PI;
  }
  return t;
}

void wRo_to_euler(const Eigen::Matrix3d& wRo, double& yaw, double& pitch, double& roll) 
{
    yaw = standardRad(atan2(wRo(1,0), wRo(0,0)));
    double c = cos(yaw);
    double s = sin(yaw);
    pitch = standardRad(atan2(-wRo(2,0), wRo(0,0)*c + wRo(1,0)*s));
    roll  = standardRad(atan2(wRo(0,2)*s - wRo(1,2)*c, -wRo(0,1)*s + wRo(1,1)*c));
}


string print_detection(AprilTags::TagDetection& detection)  
{
    //cout << "  Id: " << detection.id << " (Hamming: " << detection.hammingDistance << ")";

    // recovering the relative pose of a tag:

    // NOTE: for this to be accurate, it is necessary to use the
    // actual camera parameters here as well as the actual tag size
    // (m_fx, m_fy, m_px, m_py, m_tagSize)
    string str_buff="";
    Eigen::Vector3d translation;
    Eigen::Matrix3d rotation;
    detection.getRelativeTranslationRotation(m_tagSize, m_fx, m_fy, m_px, m_py, translation, rotation);

    Eigen::Matrix3d F;
    F <<
      1, 0,  0,
      0,  -1,  0,
      0,  0,  1;
    Eigen::Matrix3d fixed_rot = F*rotation;
    double yaw, pitch, roll;
    wRo_to_euler(fixed_rot, yaw, pitch, roll);
	/*printf("ID:%d",detection.id);
	printf("x:%f",translation(0));
	printf("y:%f",translation(1));
	printf("z:%f",translation(2));
	printf("yaw:%f",yaw);
	printf("pitch:%f",pitch);
	printf("roll:%f",roll);*/
    str_buff+=to_string(detection.id);//ID
    str_buff+="|";
    str_buff+=to_string(detection.cxy.first);//x
    str_buff+="|";
    str_buff+=to_string(detection.cxy.second);//y
    str_buff+="|";
    str_buff+=to_string(detection.getXYOrientation());//XYOrientation
    str_buff+="|";
    str_buff+=to_string(translation.norm());//distance
    str_buff+="|";
    str_buff+=to_string(translation(0));//xm
    str_buff+="|";
    str_buff+=to_string(translation(1));//ym
    str_buff+="|";
    str_buff+=to_string(translation(2));//zm
    str_buff+="|";
    str_buff+=to_string(yaw);//yaw
    str_buff+="|";
    str_buff+=to_string(pitch);//pitch
    str_buff+="|";
    str_buff+=to_string(roll);//roll
    return(str_buff);
}

int config(int width,int height,double fx,double fy,double tagSize)//配置摄像头参数
{
    m_width=width; // image size in pixels
    m_height=height;
    m_tagSize=tagSize; // April tag side length in meters of square black frame
    m_fx=fx; //x的像素为单位的焦距，应该等于2.97/3*1952，这个值是用毫米为单位的焦距除以x方向的感光元件的长度，乘以x方向的感光元件的像素（OV2710）
    m_fy=fy; //y的像素为单位的焦距，应该等于2.97/3*1092，这个值是用毫米为单位的焦距除以y方向的感光元件的长度，乘以y方向的感光元件的像素（OV2710）
    m_px=m_width/2; //图像的x中心位置
    m_py=m_height/2; //图像的y中心位置
}


string extractTags(int AprilTag_code,cv::Mat const& image_gray)//提取AprilTag
{
	//cv::Mat image_gray_copy;
	//image_gray.copyTo(image_gray_copy);
	//cv::cvtColor(image_gray_copy,image_gray_copy, COLOR_BGR2GRAY);
    string str_buff="";
    AprilTags::TagCodes m_tagCodes=AprilTags::tagCodes36h11;
    switch(AprilTag_code)
    {
        case APRIL_TAG_CODE_TAG16H5:
        {
            m_tagCodes=AprilTags::tagCodes16h5;
            break;
        }
        case APRIL_TAG_CODE_TAG25H7:
        {
            m_tagCodes=AprilTags::tagCodes25h7;
            break;
        }
        case APRIL_TAG_CODE_TAG25H9:
        {
            m_tagCodes=AprilTags::tagCodes25h9;
            break;
        }
        case APRIL_TAG_CODE_TAG36H9:
        {
            m_tagCodes=AprilTags::tagCodes36h9;
            break;
        }
        case APRIL_TAG_CODE_TAG36H11:
        {
            m_tagCodes=AprilTags::tagCodes36h11;
            break;
        }
    }
    AprilTags::TagDetector m_tagDetector=AprilTags::TagDetector(m_tagCodes);
    vector<AprilTags::TagDetection> detections = m_tagDetector.extractTags(image_gray); 
    if(detections.size()>0)
    {
        for (int i=0; i<detections.size();i++) 
        {
            if(i<detections.size()-1)
            {
                str_buff+=print_detection(detections[i])+"\n";
            }
            else
            {
                str_buff+=print_detection(detections[i]);
            }
        } 
    }
	return(str_buff);
}


