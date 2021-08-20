#!/bin/sh

# Camera setup
sudo apt-get install network-manager -y # headless mode only
sudo apt-get install tshark -y

# Environment setup
	#none

# Microphone setup
sudo apt-get install libportaudio2 -y
sudo apt-get install gcc gfortran python3-dev libopenblas-dev liblapack-dev libfreetype6-dev python3-tk -y # pyAudioAnalysis
sudo apt-get install llvm-10* -y # Librosa
