from distutils.core import setup
import py2exe

import os

mp3_files = []
mp3_dir = "mp3"
for item1 in os.listdir(mp3_dir):
    full_lang_dir_path = "{}/{}".format(mp3_dir, item1)
    if os.path.isdir(full_lang_dir_path):
        for item2 in os.listdir(full_lang_dir_path):
            full_file_path = "{}/{}/{}".format(mp3_dir, item1, item2)
            if os.path.isfile(full_file_path):
                input = full_lang_dir_path, [full_file_path]
                mp3_files.append(input)

setup(
    windows=['time_notifier.py'], #uncomment to work in background
    # console=['time_notifier.py'], #uncomment to work in console window
    data_files = mp3_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)