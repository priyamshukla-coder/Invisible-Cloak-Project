import cv2
##this is webcam
cap=cv2.VideoCapture(0)##reading image from webcam so 0 parameter
while cap.isOpened():
    ret,back=cap.read()##Simply reading background
    if ret:
        cv2.imshow("image",back)
        ##back is a varible which is used to store what camera is  reading
        if ret:
            cv2.imshow("image",back)
            ##window which popped out
            if cv2.waitKey(5)==ord('q'):
                cv2.imwrite("image.jpg",back)
                break
cap.release()
cv2.destroyAllWindows()