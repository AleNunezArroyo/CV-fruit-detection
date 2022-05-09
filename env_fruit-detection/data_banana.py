
# import the opencv library
import cv2 
import time
import os
# define a video capture object

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
    
    # path = '/home/ale/Desktop/nDATASET/con_fondo_bolsa_banana'
    path = '/home/ale/Desktop/nDATASET/con_fondo_bolsa_granadilla'
    
    # time.sleep(6)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        # 1
        # cv2.imwrite(os.path.join(path , 'fruta_con_fondo_bolsa_banana'+str(counter)+'.png'),frame1)
        # cv2.imwrite(os.path.join(path , 'numero_con_fondo_bolsa_banana'+str(counter)+'.png'),frame2)
        cv2.imwrite(os.path.join(path , 'fruta_con_fondo_bolsa_granadilla'+str(counter)+'.png'),frame1)
        cv2.imwrite(os.path.join(path , 'numero_con_fondo_bolsa_granadilla'+str(counter)+'.png'),frame2)
        counter = counter + 1
        print("Toma foto..")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the cap object
vid1.release()
vid2.release()
# Destroy all the windows
cv2.destroyAllWindows()