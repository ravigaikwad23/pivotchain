#For reading a video file and extracts frames from it.

import cv2
cap= cv2.VideoCapture('/home/ravi/Project/project_video.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('kang'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()