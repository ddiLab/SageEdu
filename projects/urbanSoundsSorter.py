import os
import re

classes = ['air_conditioner', 'car_horn', 'children_playing', 
           'dog_bark', 'drilling', 'engine_idling', 'gun_shot',
           'jackhammer', 'siren', 'street_music']

# Iterates through all the folders in the dataset
for i in range(1,11):
    # Source folder path relative to this file
    sourceFolder = './UrbanSound8K/audio/fold' + str(i) + '/'
    fileList = os.listdir(sourceFolder)

    # Iterates through all the classes in the dataset
    for c in range(0,10):
        # Make destination folder
        destFolder = './UrbanSound8K/' + classes[c] + '_files'
        os.mkdir(destFolder)
        print('Made Folder: ', destFolder)

        # Audio file name format:
        # [fsID]-[classID]-[occurrenceID]-[sliceID].wav
        # Matches classID
        pattern = r'\d+-' + str(c) + r'-\d+-\d+.wav'

        #Iterates through all the files in the folder
        for file in fileList:
            if re.search(pattern, file):
                # move file from to folder
                os.rename(sourceFolder + file, destFolder + file)