#!/usr/bin/env python2
import cv2
import numpy as np
import re
import argparse

#video_src = cv2.VideoCapture('http://192.168.43.22:8000/cam.mjpg') #ip webcam andorid use IP (Webcam_1.9.12r.apk)
#video_src = cv2.VideoCapture(0) #camera host

cascade_src = 'cars.xml'
video_src = 'video1.avi' #video file

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

img0 = cv2.imread('deep-learning-importance.png') #1024*742 <----image Size

cv2.namedWindow("Atlantes", cv2.WINDOW_NORMAL)

#################Size_video_ || cam#########-H https://www.facebook.com/atlantes.land

Width = 320#640#
Height = 240#480#
###################end##########################

######################
kgh =0
rack =1
trak =0
arm1 =0
srt =0
i = str(0)
plm =str(1)
#########################
#
x1,x2,x3,x4=(50 ,55 ,80 ,144)

while True:
   
  img = cv2.imread('deep-learning-importance.png') #1024*742 <----image Size
##########end if 1
########if 2
  trak =trak+1
  if trak > 50:
    trak =14
##########end if 2
  #cv2.createButton('Button',i)
######################y = 0>>>500
#################config cam or video1???_and dec____car.1,2,3,4,5,6........
  ret, frame = cap.read()
  if (type(frame) == type(None)):
      break
  thresh = cv2.threshold(frame, 65, 255, cv2.THRESH_BINARY)[1]
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cars = car_cascade.detectMultiScale(gray, 1.1, 1)

  #cv2.line(frame,(6,122),(260,122),(0,0,0),2)
  #cv2.line(frame,(6,95),(260,95),(255,0,0),2)
################################################################
  cv2.line(frame,(81,55),(149,55),(0,0,0),2)####<-----------<
  cv2.line(frame,(6,122),(77,58),(0,0,0),2)
  cv2.line(frame,(12,122),(100,122),(0,0,0),2)
  cv2.line(frame,(100,122),(149,55),(0,0,0),2)

######################################################################
##          (77,8) >> O---------------------------O << (8,133)             #####
#########point1 y|<,x^-,pn2<y,x^-||||||||good
  cv2.line(frame,(144+8,55),(144+80,55),(0,0,0),2)
  cv2.line(frame,(144+70,122),(144+80,58),(0,0,0),2)
  cv2.line(frame,(144+70,122),(77,122),(0,0,0),2)
 
##############################################################################
  for (x,y,w,h) in cars:
      if kgh == 150:  
        img =img0
      cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,0,255),2)   

      print x   
      hh = '{0}' .format(len(cars)) 
      string1 = hh
      kkll = int(re.search(r'\d+', string1).group())   
           
      cv2.rectangle(frame,(0,29),(39,0),(0,0,255),-1)
      if kkll > 0 and y <72 and y >62:
        rack = rack +1
        arm1 = arm1+kkll

        for rtm in range (kkll):
          srt = srt+rtm
 
      if y <122 and y >71:
         #cv2.line(frame,(14,122),(260,122),(0,255,0),2)
         #cv2.line(frame,(6,95),(260,95),(0,255,0),2)
         ################################################################
         cv2.line(frame,(81,55),(149,55),(0,255,0),4)####<-----------<
         cv2.line(frame,(6,122),(77,58),(0,255,0),4)
         cv2.line(frame,(12,122),(100,122),(0,255,0),4)
         cv2.line(frame,(100,122),(149,55),(0,255,0),4)

######################################################################
##          (77,8) >> O---------------------------O << (8,133)             #####
#########point1 y|<,x^-,pn2<y,x^-||||||||good
         cv2.line(frame,(144+8,55),(144+80,55),(0,255,0),4)
         cv2.line(frame,(144+70,122),(144+80,58),(0,255,0),4)
         cv2.line(frame,(144+70,122),(77,122),(0,255,0),4)
 
##############################################################################
  cv2.putText(img,
  'total_It is not true :',
  (4, 250), cv2.FONT_HERSHEY_PLAIN,3,(0, 255, 0))

  cv2.putText(frame,
  '%d' % (kkll),
  (30, 118), cv2.FONT_HERSHEY_PLAIN,3,(0, 0, 0))
  cv2.putText(img,
  '(%s)' % (rack),
  (8, 300), cv2.FONT_HERSHEY_PLAIN,3,(0, 0, 255))
###########################np_pix############################  
  img[600-Height:600, 1000-Width:1000] = thresh   
  img[280-Height:280, 1000-Width:1000] = thresh
  img[600-Height:600, 1000-Width:1000] = frame
####################################print_all######################################
  cv2.imshow('Atlantes',img)
  key = cv2.waitKey(10)
  if key == 27: 
      break 

