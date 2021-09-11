# Librosa setup
Archived and not necessary for this project

2. **can be archived** The librosa library will require packages not included in its installation (e.g., numpy, audioread, scikit-learn). So to ensure a smooth installation, install pyAudioAnalysis first. Or you can take a look at the [setup requirements](https://github.com/librosa/librosa/blob/90cef6fb5a38261eb2076d3e00aad4927400353f/setup.cfg) and install them individually

## Librosa **can be archived**
1. Make sure the system is up-to-date and you have the required packages installed
2. Outside of the virtual environment (if using one), run `sudo apt-get install llvm-10*`
3. Run `sudo -i`
4. Run `cd /usr/bin/`
5. Run `rm llvm-config` (if the file exists)
6. Run `ln -s llvm-config-10 llvm-config`
    1. This will redirect the llvm-config file to llvm-10, which is necessary to install llvmlite (a dependency for the librosa library)
7. Refresh the terminal and go back to where the library and accompanying packages should be installed
8. Run `pip install librosa`
9. Note: installing librosa is now available in any virtual environment with the root changes implemented above
10. Refer to the library's [website](https://librosa.org) for more information
