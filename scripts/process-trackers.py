##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import shutil
import yaml
from termcolor import colored

# PATHS
app_path = os.path.abspath('..')
data_path = app_path + '/_data/tracks/'
destination_path = app_path + '/_tracks/'

#reset destination folder
if os.path.exists(destination_path):
    shutil.rmtree(destination_path)
os.makedirs(destination_path)

# get all directories
(_, _ , files) = next(os.walk(data_path))


for file in files:
    # create track directory
    filename = file.split(".")
    track_path = destination_path + filename[0]

    if not os.path.exists(track_path):
        os.makedirs(track_path)
        print("file " , track_path,  colored(" Created", 'cyan'))
    else:    
        print("file " , track_path ,  colored(" already exists", 'green'))
    
    # create tracker index page  
    path = track_path + '/index.md'
    if not os.path.exists(path):
        index_content = "---\ntrack_name: " + filename[0] + "\nlayout: track" + "\nslug: " + filename[0] + "_index" + "\n---"
        with open(path, 'w') as f:
            f.write(index_content)
        print("Index file " , path,  colored(" Created", 'cyan'))
    else:    
        print("Index file " , path ,  colored(" already exists", 'green'))  


