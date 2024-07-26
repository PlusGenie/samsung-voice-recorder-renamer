# Samsung Voice Recorder File Renamer and Downloader

This script pulls voice recording files from a specified directory on a Samsung Android device, renames them based on their creation timestamp, replaces spaces in filenames with underscores, and saves them to a specified local directory.

## Features

- Automatically retrieves files from the Samsung Voice Recorder app directory.
- Renames files based on their creation timestamp.
- Replaces spaces in filenames with underscores for better compatibility.
- Allows specifying custom source and target directories.

## Usage

./rename_voice_recorder.py [source_directory] [local_directory]


### Default Values

- **Source Directory:** `/storage/06F4-1631/Recordings/Voice Recorder`
- **Local Directory:** `./voice_recorder_temp`

### Examples


- Use default directories:
./rename_voice_recorder.py

- Specify custom directories:
./rename_voice_recorder.py "/new/source/directory" "./new_local_directory"

## Requirements

- Python 3.x
- ADB (Android Debug Bridge) installed and configured on your system.
- Proper USB debugging permissions and connectivity between your computer and the Samsung Android device.

## Installation

1. Ensure you have Python 3 and ADB installed on your system.
2. Clone this repository.
3. Make the script executable:
- chmod +x rename_voice_recorder.py


## Script Explanation

This script is designed to automate the process of retrieving and renaming voice recording files from the Samsung Voice Recorder app on an Android device. The script performs the following steps:

1. Reads the source and target directories from command line arguments or uses default values.
2. Ensures the local target directory exists.
3. Lists files in the source directory on the Android device.
4. Retrieves the creation timestamp for each file.
5. Renames the files based on their creation timestamp, replacing spaces with underscores.
6. Pulls the renamed files to the local target directory.

## Contact

For any questions or issues, please open an issue on the GitHub repository.