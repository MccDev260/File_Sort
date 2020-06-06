import os.path
import shutil

folder_path = "" # Invert slashes in folder path

images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for image in images:
    folder_name = image.split(' ')[0] # Use this to choose how to sort files

    new_path = os.path.join(folder_path, folder_name)

    old_image_path = os.path.join(folder_path, image)

    if not os.path.exists(new_path):
        os.makedirs(new_path)
        new_image_path = os.path.join(new_path, image)
        shutil.move(old_image_path, new_image_path)
    
    else:
        shutil.move(old_image_path, new_path)