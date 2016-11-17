# -*- coding: utf-8 -*-

import cv2 ##إستدعاء المكتبة الرئيسية cv2


cascade_src = 'cars.xml' ####ملف الاحتمالات الوسوم##
#video_src = 'mmn.3gp'
video_src = 'video1.avi' ####ملف الفيديو#####

cam11 = cv2.VideoCapture(video_src)

car_cascade = cv2.CascadeClassifier(cascade_src)# إسناد ملف الوسوم 

while True:
    ret, img = cam11.read() # cam القراءة من ال 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ##تحويل الي الابيض والاسود
    
    cars = car_cascade.detectMultiScale(gray, 1.2, 1) ##البحث عن السيارات وإسناد القيم إلي المصفوفة cars
##############################################


    for (x,y,w,h) in cars: #التكرار بداخل المصفوفة باسناد إلي القيم x,y,w,h
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   #رسم مربع حول السيارات باستخدام القيم السابقة واعطاء اللون والحجم بداخل ال img   

#######################################################https://www.facebook.com/eman.faruk.7?fref=ufi
    cv2.imshow('openssh', img)###عرض نافذة تحمل الفيديو مع كل التعديلات السابقة 
    
    if cv2.waitKey(33) == 27:#إنتظار المستخدم حتي يضغط علي المفتاحEsc
        break  ##ثم الايقاف ولكنه في الحقيقة يتوقف عندما ينتهي الفيديو

cv2.destroyAllWindows() ##تحرير المساحة المستخدمة من قبل ال cv2
