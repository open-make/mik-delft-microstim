from pypylon import pylon
import cv2
import os
from capture_behaviour import *
from datetime import date

# Please specify the serial number of the Basler camera you want to record with. 
# You can find the serial number on the camera itsself. 
WhiskerCam_serial = '22523118' 
camera = findCamera(WhiskerCam_serial)
camera.Open()

# Set camera parameters (e.g., frame rate, exposure time) # TODO is there a setup file for this?    
fps = 200 # Frames per second
preFrame, postFrame = (200, 400) # How many frames before and how many after the trigger?
camera.AcquisitionFrameRateEnable.SetValue(True)
camera.AcquisitionFrameRate.SetValue(fps)
camera.ExposureAuto.SetValue("Off")
camera.ExposureTime.SetValue(3000)
camera.MaxNumBuffer = 1000
camera.MaxNumBuffer.SetValue(1000)
camera.Width = 992
camera.Height = 750
camera.LineSelector ='Line3' # On which line of the GPIO does the trigger arrive?
camera.LineMode = 'Output'

# Define each filename, start grabbing frames and run the code
fileName_blank = input('Please type the SNA/MLA animal ID here:')
today = date.today()
today = today.strftime('%d_%m_%Y') + '/'
saveFolder = 'D:/Users/Mik/mStim_data/PSI/' + fileName_blank + '/microstim/Videos/whisker/' + today
# saveFolder = 'C:/Users/miksc/Desktop/Videos'  + fileName_blank + '/microstim/Videos/whisker/' + today
os.makedirs(saveFolder, exist_ok=True)

# saveFolder = 'D:/Users/Mik/mStim_data/PSI_Videos/'
# fileName_blank = 'SNA-123996' # Animal ID

feature = '_whisker'
trigger_method = 'hardware' # Set this to 'software' and press 'T' to trigger, or 'hardware' and use GPIO

# Start frame aquisition and capture behavioural videos
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
iTrial = 0
while True:
    fileName = fileName_blank + feature + '_' + str(iTrial)
    capture_behaviour(camera, saveFolder+fileName, fps, (preFrame, postFrame), trigger=trigger_method )
    iTrial += 1

    if cv2.waitKey(1) == ord('q'): # Press 'Q' to exit
        break
    
# Release resources
camera.StopGrabbing()
camera.Close()
cv2.destroyAllWindows() 
