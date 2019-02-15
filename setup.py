from distutils.core import setup
import py2exe

mp3_files = [('mp3/eng-emma', ['mp3/eng-emma/test.mp3'])]

setup(
    console=['time_notifier.py'],
    data_files = mp3_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "excludes": ["email"]
                }
        }
)