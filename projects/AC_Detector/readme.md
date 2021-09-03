# AC_Detector directory
This folder contains installation instructions for creating a virtual environment to house all the work done in this directory, installing an audio analysis library, and developing an AC detector using AI and data analysis   
Get started with 
1. [setup](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/setup.md)
2. [reviewing the pyAudioAnalysis tutorial](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/pyAudioAnalysisIntroduction.ipynb)

And afterwards, explore the directory!

---

## [audio_training_dataset/](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/audio_training_dataset)
* directory with the data needed to train an AI model in audio detection using the `AC AI.iypnb` notebook
* note: it does not include the urbanSounds dataset because it was too large

## [collected_data/](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/collected_data)
* directory that stores all the collected temperature and audio data, along with the analysis of that data produced by the `ACDetector.ipynb` notebook

## [initial_test_programs](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/urbanSounds)
* directory that stores initial test programs used in the creation of the current project

## [urbanSoundsMEANS](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/urbanSoundsMEANS)
* a binary file that stores audio classifer information of the previously trained AI model

## [urbanSounds](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/urbanSounds)
* a binary file that stores audio classifer information of the previously trained AI model

## [urbanSounds.arff](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/urbanSounds.arff)
* a plain text file that stores audio classifer information of the previously trained AI model

## [setup_script.sh](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/setup_script.sh)
* shell program that entirely sets up the necessary virtual environment with packages specifically for this project 

## [collect_volume.py](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/collect_volume.py)
* python program that aids the collection of audio data in the `ACDetector.iypnb` notebook
* it is executable via the terminal and the following are the arguments:
	* `python3 collect_volume.py <delay> <duration> <max_time> <file_name>.csv`
	* `<delay>`: time in seconds between each audio sample taken
	* `<duration>`: time in seconds of each sample length
	* `<max_time>`: time in minutes of maximum allowed time that the script can run for
	* `<file_name>.csv`: name of the file that will stored in the directory `collected_data` in .csv format
* this program also stores the audio clips in the `collected_data/audio_samples` directory

## [collect_temp.py](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/collect_temp.py)
* python program that aids the collection of temperature data in the `ACDetector.iypnb` notebook
* it is executable via the terminal and the following are the arguments:
	* `python3 collect_temp.py <delay> <max_time> <file_name>.csv`
	* `<delay>`: time in seconds between each temperature measurement taken
	* `<max_time>`: time in minutes of maximum allowed time that the script can run for
	* `<file_name>.csv`: name of the file that will stored in the directory `collected_data` in .csv format

## [ACDetector.ipynb](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/ACDetector.ipynb)
* main notebook that collects data, graphs it, and analyzes it with the trained AI model to detect an AC

## [AC AI.ipynb](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/AC%20AI.ipynb)
* a notebook that introduces how to train an AI model for audio detection
* note: the data it uses to train the model is in the directory `audio_training_dataset`

## [pyAudioAnalysisIntroduction.ipynb](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/pyAudioAnalysisIntroduction.ipynb)
* a notebook that contains instructions and code in using the `pyAudioAnalysis` library
* includes feature extraction, beat detection, and visualization with spectrograms and chromagrams

## [librosa_setup.md](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/librosa_setup.md)
* contains instructions on setting up the librosa library, but is not necessary for this project

## [setup.md](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/AudioLibrarySetup.md)
* includes instructions on setting up the virtual environment for this project and installing pyAudioAnalysis

## [readme.md](https://github.com/ddiLab/SageEdu/blob/main/projects/AC_Detector/readme.md)
* this file
