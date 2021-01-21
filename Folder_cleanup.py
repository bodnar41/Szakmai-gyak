import os
import collections
import platform
import sys
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264']
EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'svg', 'tiff', 'tif']
EXT_DOCS  = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']


# Create directories where we want to store the files
BASE_PATH = os.path.expanduser("~")
DEST_DIRS = ["Music", "Movies", "Pictures", "Documents", "Applications", "Other"]

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

# Map files from Downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH, "Downloads")
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != ".":
        file_ext = file_name.split(".")[-1]
        files_mapping[file_ext].append(file_name)

pprint(files_mapping)

# Move all files given a file extension to a target directory
try:
    for f_ext, f_list in files_mapping.items():

        if f_ext in EXT_INSTL:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Applications", file))

        elif f_ext in EXT_AUDIO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Music", file))

        elif f_ext in EXT_VIDEO:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Movies", file))

        elif f_ext in EXT_IMGS:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Pictures", file))

        elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Documents", file))

        else:
            for file in f_list:
                os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, "Other", file))
except:
    uname = platform.uname()
    clientname = uname.node.strip('-PC')
    with open(f"C:/Users/{clientname}/Output.txt", "w") as file:
        file.write(sys.exc_info())
else:
    uname = platform.uname()
    clientname = uname.node.strip('-PC')
    with open(f"C:/Users/{clientname}/Output.txt", "w") as file:
        file.write("Cleaningup was successful!")
