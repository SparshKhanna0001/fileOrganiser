import os
from pathlib import Path
from typing import Dict, List, Optional
from shutil import move
from timer import start, time_taken
#from time import perf_counter as counter
#import asyncio

#DEFAULT ARGUMENTS
FOLDERS : Dict[str,List[str]]={
        "images": ['.png','.jpeg'],
        "videos":['mp4'],
        "documents":[".txt",".docx"],
        "audio":["mp3",".wav"],
        "other":[]
    }

#Porgam messages
path_confirmation = f"The current working directory is\n\t{os.getcwd()}\t [ENETER Y] \n\nDo you want to continue or alter [ ENTER PATH ]\n\n\tENETER INPUT : "
sorting_config = f"""
    The files will be sorted as per the following config:
    {FOLDERS}

    Sorting begins....
"""
sorting_complete = f"""
    Sorting of files as per te following config:
    {FOLDERS}

    has been done
    and the time taken for that is: 
"""

#program fucntions:
def make_folders(path, folders:Dict[str,List[str]]=FOLDERS):
    try:
        for folder in folders.keys():
            (Path(path) / folder).mkdir(exist_ok=True)
    except Exception as e:
        print(e)


def path_input() -> str:
    while True:
        path = input(path_confirmation)

        if path.lower() == 'y':
            break
        elif not os.path.exists(path):
            print("WRONG_INPUT")
        else:
            break
    
    print(path)
    path = os.getcwd() if path.lower() == 'y' else path

    return path


def reverse_dictonary(folders: Dict[str, List[str]] = FOLDERS) -> Dict[str, str]:
    EXTENSIONS = dict()

    for i in list(folders.items()):
        for j in i[1]:
            EXTENSIONS[j] = i[0]
    
    return EXTENSIONS


def organiser(files: List[Path], path: str, extensions: Dict[str,str]=reverse_dictonary()) -> Optional[str]:
    for file in files:
        folder = extensions.get(file.suffix)
        try:
            if folder is not None:
                move(str(file), str(Path(path) / folder / file.name))
            else:
                folder = "other"
                move(str(file), str(Path(path) / folder / file.name))
        except Exception as e:
            print(f"ERROR MOVING {file} : {e}")


def main():
    path = path_input()
    make_folders(path)
    files = [f for f in Path(path).iterdir() if f.is_file()]
    print(sorting_config)
    start()
    organiser(files, path)
    elapsed = time_taken()
    print(f"{sorting_complete} \t{elapsed:.2f} seconds.")




if __name__ == "__main__":
    main()
