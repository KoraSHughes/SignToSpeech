#--------------------------------------------------------------------
#notes
#--------------------------------------------------------------------
#references
#  https://developer-archive.leapmotion.com/documentation/python/devguide/Leap_Images.html
#    https://developer-archive.leapmotion.com/documentation/python
#      -> using the tracking API -> Camera Images -> Correction Using bilinear interpolation
#
#--------------------------------------------------------------------
#--------------------------------------------------------------------
import cv2
import math
import ctypes
import numpy as np
import time

def convert_distortion_maps(image):

    distortion_length = image.distortion_width * image.distortion_height
    xmap = np.zeros(distortion_length/2, dtype=np.float32)
    ymap = np.zeros(distortion_length/2, dtype=np.float32)

    for ii in range(0, distortion_length, 2):
        xmap[distortion_length/2 - ii/2 - 1] = image.distortion[ii] * image.width
        ymap[distortion_length/2 - ii/2 - 1] = image.distortion[ii + 1] * image.height
    ##end for ii in range(0, distortion_length, 2):
    
    xmap = np.reshape(xmap, (image.distortion_height, image.distortion_width/2))
    ymap = np.reshape(ymap, (image.distortion_height, image.distortion_width/2))

    #resize the distortion map to equal desired destination image size
    resized_xmap = cv2.resize(xmap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)
    resized_ymap = cv2.resize(ymap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)

    #Use faster fixed point maps
    coordinate_map, interpolation_coefficients = cv2.convertMaps(resized_xmap,
                                                                 resized_ymap,
                                                                 cv2.CV_32FC1,
                                                                 nninterpolation = False)

    return coordinate_map, interpolation_coefficients
##end def convert_distortion_maps(image):

def undistort(image, coordinate_map, coefficient_map, width, height):
    destination = np.empty((width, height), dtype = np.ubyte)

    #wrap image data in numpy array
    i_address = int(image.data_pointer)
    ctype_array_def = ctypes.c_ubyte * image.height * image.width
    # as ctypes array
    as_ctype_array = ctype_array_def.from_address(i_address)
    # as numpy array
    as_numpy_array = np.ctypeslib.as_array(as_ctype_array)
    img = np.reshape(as_numpy_array, (image.height, image.width))

    #remap image to destination
    destination = cv2.remap(img,
                            coordinate_map,
                            coefficient_map,
                            interpolation = cv2.INTER_LINEAR)

    #resize output to desired destination size
    destination = cv2.resize(destination,
                             (width, height),
                             0, 0,
                             cv2.INTER_LINEAR)
    return destination
##end def undistort(image, coordinate_map, coefficient_map, width, height):

def run(controller,dirParent,dirTrial,freqDesired,duration,isImShow):
    deltaDesired = float(1)/float(freqDesired)
    maps_initialized = False
    ii=0
    timeLastWrite = time.time() #unix time
    timePrevIt = timeLastWrite
    timeStart = time.time()
    while (True):
        timeTot = time.time()
        if not duration == -1: #if -1, press ctl-c to quite program
            if timeTot - timeStart > duration: #debug
                print("total images = {}".format(ii))
                break
            ##end if timeTot - timeStart > 10:
        ##end if not duration == -1:
        frame = controller.frame()
        image = frame.images[0]
        if image.is_valid:
            if not maps_initialized:
                left_coordinates, left_coefficients = convert_distortion_maps(frame.images[0])
                right_coordinates, right_coefficients = convert_distortion_maps(frame.images[1])
                maps_initialized = True
            ##end if not maps_initialized:

            timeCurIt = time.time()
            timeLastIt = timeCurIt - timePrevIt #time it took to do the last iteration of writing
            timePrevIt = timeCurIt #set for next round
            deltaSinceWrite = timeCurIt - timeLastWrite #time since beg of last write
            timeThresh = deltaDesired - timeLastIt #with timeLastIt
            #timeThresh = deltaDesired #without timeLastIt
            if deltaSinceWrite >= timeThresh: 
                timeLastWrite = time.time()
                undistorted_left = undistort(image, left_coordinates, left_coefficients, 400, 400)
                undistorted_right = undistort(image, right_coordinates, right_coefficients, 400, 400)

                ##7 digits is enough for 24 hrs
                #filename0 = dirTrial + '{:08}_0.png'.format(ii)
                #filename1 = dirTrial + '{:08}_1.png'.format(ii)
                filename0 = dirTrial + '{:.6f}_0.png'.format(timeCurIt)
                filename1 = dirTrial + '{:.6f}_1.png'.format(timeCurIt)
                
                cv2.imwrite(filename0, undistorted_left)
                cv2.imwrite(filename1, undistorted_right)

                if isImShow == True:
                    cv2.imshow('Left Camera', undistorted_left)
                    cv2.imshow('Right Camera', undistorted_right)
                ##end if isImShow == True:                    

                ii = ii + 1 #set for next round
            ##end if deltaSinceWrite >= deltaDesired:

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            ##end if cv2.waitKey(1) & 0xFF == ord('q'):
        ##end if image.is_valid:
    ##end while (True):
##end def run(controller):

