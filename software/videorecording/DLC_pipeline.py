import deeplabcut
import os







if __name__ == '__main__':
    root = 'G:/mStim_data/PSI/'

    # Select animals or do whole folder
    # IDs = os.listdir(root)
    IDs = ['SNA-126687']

    # (Un)comment to select correct feature
    # feature = 'whisker/'
    feature = 'pupil/'
    # whiskerConfig = "E:/WhiskerTrackerV3-Schutte-2023-08-15/config.yaml"
    pupilConfig = 'G:/MicrostimPupilTracker-Schutte-2022-05-17/config.yaml'

    # Go through it
    for ID in IDs:
        print(ID)
        dates = os.listdir(root+ID+'/microstim/' + 'Videos/' + feature)
        print(dates)
        
        for date in dates:
            if date == '17_10_2023':
                videoPath = root+ID+'/microstim/' + 'Videos/' + feature + date 
                videoFiles = [file for file in os.listdir(videoPath) if file.endswith('mp4v')]
                videoFilePaths = [videoPath + '/' + file for file in videoFiles] 

                # For Whisker
                # deeplabcut.analyze_videos(whiskerConfig, videoFilePaths)   
                # deeplabcut.create_labeled_video(whiskerConfig, videoFilePaths)     

                # For Pupil 
                # deeplabcut.analyze_videos(pupilConfig, videoFilePaths)      
                deeplabcut.create_labeled_video(pupilConfig, videoFilePaths)  
                        
