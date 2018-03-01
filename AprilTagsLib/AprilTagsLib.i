%module AprilTagsLib
%include <opencv.i>

%include "std_string.i"
%include "carrays.i"
%cv_matx_instantiate_defaults
%{
    #include "AprilTagsLib.hpp"
%}
%include "AprilTagsLib.hpp"

