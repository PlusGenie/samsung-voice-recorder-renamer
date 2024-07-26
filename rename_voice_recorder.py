#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

# Local temporary directory
local_directory = "./voice_recorder_temp"
source_directory = "/storage/06F4-1631/Recordings/Voice Recorder"

# Ensure the local temporary directory exists
os.makedirs(local_directory, exist_ok=True)

# Function to get file creation time from the device
def get_creation_time(file_path):
    print(f"Entering get_creation_time for {file_path}")
    command = f'adb shell stat -c %Y \\"{file_path}\\"'
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to get creation time for {file_path}: {result.stderr}")
        return None
    creation_time = int(result.stdout.strip())
    print(f"Exiting get_creation_time for {file_path} with {creation_time}")
    return creation_time

# Function to pull and rename files from the device
def pull_and_rename_files(source_directory, local_directory):
    print(f"Entering pull_and_rename_files for {source_directory}")
    escaped_source_directory = source_directory.replace(" ", "\\ ")
    command = f'adb shell ls -a "{escaped_source_directory}"'
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to list directory {source_directory}: {result.stderr}")
        return
    files = result.stdout.strip().split('\n')
    print(f"Files found: {files}")

    for file_name in files:
        if file_name and file_name not in ['.', '..']:  # Ensure the file_name is not empty and not current/parent directory
            original_file_path = f"{source_directory}/{file_name}"
            creation_time = get_creation_time(original_file_path)
            if creation_time is None:
                continue  # Skip files where creation time couldn't be determined
            creation_time_str = datetime.fromtimestamp(creation_time).strftime('%Y_%m_%d_%H:%M')

            # Generate new file name with spaces replaced by underscores
            base_name, ext = os.path.splitext(file_name)
            base_name = base_name.replace(" ", "_")
            new_file_name = f'{creation_time_str}_{base_name}{ext}'
            local_file_path = os.path.join(local_directory, new_file_name)

            # Pull the file to local machine with new name
            pull_command = f'adb pull "{original_file_path}" "{local_file_path}"'
            print(f"Running command: {pull_command}")
            pull_result = subprocess.run(pull_command, shell=True)
            if pull_result.returncode == 0:
                print(f'Pulled and renamed: {file_name} -> {new_file_name}')
            else:
                print(f'Failed to pull: {file_name}')
    print(f"Exiting pull_and_rename_files for {source_directory}")

# Main entry point
if __name__ == "__main__":
    print("Starting the script")
    pull_and_rename_files(source_directory, local_directory)
    print("Script finished")
