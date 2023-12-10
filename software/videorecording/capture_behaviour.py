from pypylon import pylon
import cv2
import numpy as np
from queue import Queue

def capture_behaviour(camera, fileName, fps, frameSet, trigger='hardware', resize=False): #TODO Add a Triggered once thing, the TTL is too long
    ''' This function allows for the continuous aquisition of frames. Frames are being put in a queue and the
        location of the triggered frame is defined by the frameSet, settings.
    
        INPUT:
            camera (pylon.InstantCamera): Opened camera device that you want to grab in loops
            fileName (str): Name of the .mp4 file, often ideally structured as ID_sesh_trialnumber
            fps (int/float): Frames per second you want to aquire 
            frameSet (tup): Number of frames you want before and after the trigger (preFrame, postFrame)
            trigger (str): Trigger through hardware or software, default is hardware, if software press T
            
        OUTPUT: 
            singleTrialbehaviour (.mp4): A video file, stored in the root folder that depicts single trial behaviour
    '''
    # Prepare fileName and unpack values
    fileName = fileName + '.mp4v'
    frame_count = 0
    preFrame, postFrame = frameSet
    frame_total = sum(frameSet) 
    triggered = False
    frameQueue = Queue(maxsize = frame_total)
    
    # Start continuous acquisition
    while camera.IsGrabbing() and frame_count < postFrame: 
        # Check if the queue is full
        if frameQueue.full():
            removedFrame = frameQueue.get()
            
        # Grab a frame through the instantiated camera, if succesful place into the frameQueue
        grab_result = camera.RetrieveResult(1000, pylon.TimeoutHandling_ThrowException)
        if grab_result.GrabSucceeded():
            frame = grab_result.Array
            frameQueue.put(frame)

            # Show a preview of what is being aquired
            if resize:
                frameShow = cv2.resize(frame, (512, 640))
                cv2.imshow("Preview", frameShow)
            else:
                cv2.imshow('Preview', frame)
            # If the camera has been triggered start ramping up the frame count
            if triggered:
                frame_count += 1
            
            # Check for trigger input and mark the frame
            key = cv2.waitKey(1) & 0xFF
            if trigger == 'hardware':
                if camera.LineStatus() and triggered == False:
                    print('Triggered')
                    triggered = True
                    cv2.putText(frame, 'T', (70,50), cv2.FONT_HERSHEY_PLAIN, 3,
                                (255, 0, 0), 3)

            else: # use software trigger by pressing t
                if key == ord('t'):
                    print('TRIGGERED')
                    triggered = True
                    cv2.putText(frame, 'T', (70,50), cv2.FONT_HERSHEY_PLAIN, 3,
                                (255, 0, 0), 3)

        # Release the grabbed frame
        grab_result.Release()

    # Instantiate the fourcc and videowriter with the right name, fps and size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Whats difference between mp4v, x264 and h264?
    out = cv2.VideoWriter(fileName, fourcc, float(fps), (camera.Width.Value, camera.Height.Value)) # Flipping does not help corruption

    # Convert the frameQueue into an np.array, go through all frames and write to a .mp4 file
    frameQueue = np.array(frameQueue.queue)
    for frame in frameQueue:
        out.write(frame)
    out.release()
    return

def display_video(path):
    ''' Open and play a videofile
        INPUT: 
            path(str): path to video (.mp4, .avi) file.
    '''
    # Create a VideoCapture object and read from input file
    # It needs a video file or camera path
    cap = cv2.VideoCapture(path)

    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow('Frame',frame)
            cv2.waitKey(0)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        # Break the loop
        else: 
            break
    
    # When everything done, release the video capture object and close all the frames
    cap.release()
    cv2.destroyAllWindows()
    return

def findCamera(SerialNumber_desired=None): 
    '''' Finds your Basler camera based on serial number.

        INPUT:
            SerialNumber_desired(str): the serial number of the camera you want to open. If none is given
                                       open up the first detected device.
        OUTPUT:
            camera(pylon.InstantCamera): pylon Class for handling basler cameras.
    '''
    # Manage input, by converting potential integer to string
    if isinstance(SerialNumber_desired, int):
        SerialNumber_desired = str(SerialNumber_desired)

    if SerialNumber_desired:
        # Find all connected Basler cameras 
        tlf = pylon.TlFactory.GetInstance()
        devs = tlf.EnumerateDevices()
        if len(devs) == 0:
            raise UserWarning('No cameras detected.')

        # Select camera on serial number, the serial number can be found on the camera itsself.
        for dev in devs:
            SerialNumber = dev.GetSerialNumber()
            if SerialNumber == SerialNumber_desired: 
                camera = pylon.InstantCamera(tlf.CreateDevice(dev))
                return camera
        raise UserWarning('The camera with the SerialNumber you desire is not detected.')
    
    # If no serial number has been provided, just open the first instance of the camera
    else: 
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    return camera

def createFolder():
    '''docstring
    '''
    pass
