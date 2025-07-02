from os import system
from typing import Dict, List


FOLDERS : Dict[str,List[str]]={
        "images": ['.png','.jpeg'],
        "videos":['mp4'],
        "documents":[".txt",".docx"],
        "audio":["mp3",".wav"],
        "other":[]
    }


for i in list(FOLDERS.keys()):
    system(f"rmdir {i}")

