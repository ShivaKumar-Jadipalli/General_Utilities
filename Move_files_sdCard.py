'''
This file can move all files from a particular sd card or hard disk to a single folder so that it will be easy for you to add or delete files which you don't like , It can save you a ton of time going through each and every folder to see if it useful or not 
'''

from pathlib import Path
import shutil
source_directory = Path(r'mention your source      location here')
destination_path = Path(r'mention your destination location here')
def start_work(new_path_func):
    for sub_folder in new_path_func.iterdir(): # the iterdir is used to go through all the files in the folder 
        if sub_folder.is_dir():
            start_work(sub_folder)
        else:
            shutil.copy2(sub_folder, destination_path / sub_folder.name) # the difference between copy and copy2 is that it copy2 copies along with metadata like the creating date time and all other resources like file access and everything 
for new_path in source_directory.iterdir():
    if new_path.is_dir():
        start_work(new_path)
    else:
        shutil.copy2(new_path, destination_path / new_path.name)
