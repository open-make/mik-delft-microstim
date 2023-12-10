''''Code that checks if the videos are of sufficient quality
'''

import cv2
import numpy as np
import pandas as pd
import os

def checkVideo(videoFile, frameSet, show=False):
    '''' Opens the video 1 frame before the supposed trigger Frame and compares the top left
         corner to that of the next frame. If all is correct the next frame should have a white
         'T' there, confirming the correct trigger frame conform the frameSet.

         INPUT:
            videoFile (str): Path to the video you want to check
            frameSet (tup): Number of frames you want before and after the trigger (preFrame, postFrame)
            show (bool): If the triggered Frame is not correct it gives a popup for you to check

         OUTPUT:
            checkDict (dict) TODO to pd.df: a dictionary with keys, trigger and total frames and value bool if it was correct
    '''
    # Open and check the video file
    print(f'Validating the quality of {videoFile}.')
    cap = cv2.VideoCapture(videoFile)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return False

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    correctFrameCount = total_frames == np.sum(frameSet) # It should be equal to the sum of pre and post frames
    if not correctFrameCount:
        print(f"Warning: Does not correspond to the frameSet! \n Only {total_frames} frames were found.")
        
    # Go to the specified triggerFrame 
    preFrame, postFrame = frameSet
    triggerFrame = preFrame - 1 # Should be the frame that has the 'T'
    iFrame = preFrame - 2 # -2 because preFrame starts from 1, but cv2 indexing from 0. We want to be 1 frame before


    # Read the supposed pre-trigger frame and get white values to compare with next (trigger?) frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, iFrame) 
    ret, frame = cap.read()
    top_left_region = frame[10:50, 70:100]
    prev_white_pxl = np.sum(top_left_region == 255)

    # Now read supposed trigger frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, triggerFrame) 
    ret, frame = cap.read()
    top_left_region = frame[10:50, 70:100]
    white_pxl = np.sum(top_left_region == 255)

    # The number of white pixels of the trigger frame should be higher (rougly 500) because a 'T' was placed there during recording
    white_diff = white_pxl - prev_white_pxl # Should be > 500
    correctTriggerFrame = white_diff >= 500
   
    # Press SPACEBAR once to go to the triggered frame you should see a T appear
    if show and not correctTriggerFrame:
        # Lets show the pre trigger frame first and go to the supposed trigger frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, iFrame)
        for _ in range(2):
            ret,frame = cap.read()

            # Break if the video has ended
            if not ret:
                print('End of video.')
                break

            # Display the current frame
            cv2.imshow('Video Frame', frame)
            cv2.waitKey(0)

            # Press Q on keyboard to  exit #TODO why dis never works?
            if cv2.waitKey(25) & 0xFF == ord('q'):
                print("Video playback interrupted.")
                break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return correctFrameCount and correctTriggerFrame


if __name__ == '__main__':
    # Go to the folder which contains all videoFiles
    ID = 'SNA-123996/'
    # feature = 'whisker/'
    # frameSet = (200,400)
    feature = 'pupil/'
    frameSet = (100, 200) # pupil
    sessions = os.listdir("E:/mStim_data/PSI_Videos/" + ID)

    for session in sessions:
        videoFolder = "E:/mStim_data/PSI_Videos/" + ID + session + '/' + feature
        videoFiles = [video for video in os.listdir(videoFolder) if video.endswith('.mp4v')]

        # Keep a dictionary for tracking the outcome
        checkDict = {'fileName': [], 'quality':[]}

        # Go through all videoFiles and check the quality, store outcome in dict
        for videoFile in videoFiles:
            quality = checkVideo(videoFolder + videoFile, frameSet=frameSet, show=False)
            checkDict['fileName'].append(videoFile)
            checkDict['quality'].append(quality)

        # Convert filled dictionary to dataFrame and save as .csv in the folder
        checkdf = pd.DataFrame.from_dict(checkDict)
        checkdf.to_csv(videoFolder+'qualityCheck.csv')
