import cv2


cascade_src = 'cars.xml'
#video_src = 'mmn.3gp'
video_src = 'video1.avi'

cap1 = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

cv2.namedWindow("X18.eg", cv2.WINDOW_NORMAL)

#################Size_video_ || cam#############
Width = 320#640#
Height = 240#480#
###################end##########################

while True:
    ret, img = cap1.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.2, 1)
    cv2.line(img,(6,Height/2),(Width-80,Height/2),(0,0,0),2)
    cv2.line(img,(6,Height/2-22),(Width-80,Height/2-22),(0,0,0),2)
    atlantes =(14,122),(260,122)
    ###############

    tt = "Found {0} cars!".format(len(cars))
    

    for (x,y,w,h) in cars:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)      
        print Height/2,Height/2-10,y
        
        if y <90 and y > 28:
        #if y < Height/2 and y > Height/2-10:
		## 320w,240 hei
           cv2.line(img,(6,Height/2),(Width-80,Height/2),(0,255,0),2)
           cv2.line(img,(6,Height/2-22),(Width-80,Height/2-22),(0,255,0),2)
           
    cv2.putText(img,
    '%s' % (tt),
    (8, 22), cv2.FONT_HERSHEY_PLAIN,2,(0, 255, 0))
    cv2.imshow('X18.eg', img)
    
    if cv2.waitKey(33) == 27:##out? press Esc
        break

cv2.destroyAllWindows()
####
##https://www.facebook.com/atlantes.land
