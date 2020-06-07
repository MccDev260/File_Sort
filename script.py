import os.path
import shutil

folder_path = " " # Invert slashes in folder path

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for file in files:
    folder_name = file.split(' ')[0] # Use this to choose how to sort files

    new_path = os.path.join(folder_path, folder_name)

    old_file_path = os.path.join(folder_path, file)

    if not os.path.exists(new_path):
        os.makedirs(new_path)
        new_file_path = os.path.join(new_path, file)
        shutil.move(old_file_path, new_file_path)
    
    else:
        shutil.move(old_file_path, new_path)