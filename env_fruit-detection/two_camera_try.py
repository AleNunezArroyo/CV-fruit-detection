
# import the opencv library
import cv2 
import time
import os
# define a video capture object
# pip3 install opencv-python
# pip3 install opencv-python 

# sudo apt-get install libatlas-base-dev 

# sudo apt-get install libjasper-dev 

# sudo apt-get install libqtgui4 

# sudo apt-get install python3-pyqt5 

# sudo apt install libqt4-test

vid1 = cv2.VideoCapture(0)
vid2 = cv2.VideoCapture(2)
counter = 0
while(True):
    # Capture the video frame
    # by frame
    ret1, frame1 = vid1.read()
    ret2, frame2 = vid2.read()
    
    # Display the resulting frame
    cv2.imshow('frame1', frame1)
    cv2.imshow('frame2', frame2)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    
    # path = '/home/ale/Desktop/images-test'
    path = '/home/ale/Desktop/images-test/apple'
    cv2.imwrite(os.path.join(path , 'apple'+str(counter)+'.png'),frame2)
    counter = counter + 1
    print("Toma foto..")
    time.sleep(6)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the cap object
vid1.release()
vid2.release()
# Destroy all the windows
cv2.destroyAllWindows()