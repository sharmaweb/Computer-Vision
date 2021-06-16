#pylint:disable=no-member

import cv2 as cv

capture= cv.VideoCapture(0)



haar_cascade = cv.CascadeClassifier('haar_face.xml')
while True:
    isTrue,frame=capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.imshow('Detected Faces', frame)
    if(cv.waitKey(20) & 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()



#So let's move on to essentially reading in this har underscore face dot XML file. So the way we
# do that is by essentially create a har cascade variable. 



#You can increase the minNeighbors for more accuracy
