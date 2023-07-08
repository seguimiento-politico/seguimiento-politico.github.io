##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import yaml
from termcolor import colored

# PATHS
data_trackers_path = os.getcwd() + '/_data/tracks/'
trackers_path = os.getcwd() + '/_tracks/'

# get all directories
(_, directories , _) = next(os.walk(data_trackers_path))

for directory in directories:
    if directory != "votes":
        # create track directory
        track_path = trackers_path + directory

        if not os.path.exists(track_path):
            os.makedirs(track_path)
            print("Directory " , track_path,  colored(" Created", 'cyan'))
        else:    
            print("Directory " , track_path ,  colored(" already exists", 'green'))
        
        # create tracker index page  
        path = track_path + '/index.md'
        if not os.path.exists(path):
            index_content = "---\ntrack_name: " + directory + "\nlayout: track" + "\nslug: " + directory + "_index" + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
            print("Index file " , path,  colored(" Created", 'cyan'))
        else:    
            print("Index file " , path ,  colored(" already exists", 'green'))  
                
        # create items pages
        (_, _, files) = next(os.walk(data_trackers_path + directory))
        
        for item in files:     
            if item != "settings.yaml" and item != "politicians.json":
                f = open(data_trackers_path + directory + "/" + item, "r")
                data = f.readline().strip('\n')
                f.close() 
                data = data.split(": ")
                id = data[1]
                filename = item.split(".")
                
                # create item page
                path = track_path + '/' + id + '.md'
                if not os.path.exists(path):
                    index_content = "---\ntrack_name: " + directory + "\nitem_name: " + filename[0] + "\nuid: " + id + "\nslug: " + id + "\n---"
                    with open(path, 'w') as f:
                        f.write(index_content)
                        print("Item file " , path,  colored(" Created", 'cyan'))
                else:    
                    print("Item file " , path ,  colored(" already exists", 'green'))  


