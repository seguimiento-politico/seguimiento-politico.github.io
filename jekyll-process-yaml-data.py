##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import yaml

# PATHS
data_trackers_path = os.getcwd() + '/_data/tracks/'
trackers_path = os.getcwd() + '/_tracks/'

# get all directories
(_, directories , _) = next(os.walk(data_trackers_path))

for directory in directories:
        
    # create track directory
    track_path = trackers_path + directory

    if not os.path.exists(track_path):
        os.makedirs(track_path)
        print("Directory " , track_path,  " Created ")
    else:    
        print("Directory " , track_path ,  " already exists")
    
    # create tracker index page  
    path = track_path + '/index.md'
    if not os.path.exists(path):
        index_content = "---\ntrack_name: " + directory + "\nlayout: track\n---"
        with open(path, 'w') as f:
            f.write(index_content)
        print("Index file " , path,  " Created ")
    else:    
        print("Index file " , path ,  " already exists")  
            
    # create items pages
    (_, _, files) = next(os.walk(data_trackers_path + directory))
    
    for item in files:     
        if item != "settings.yaml":
            filename = item.split(".")
            
            # create item page
            path = track_path + '/' + filename[0] + '.md'
            if not os.path.exists(path):
                index_content = "---\ntrack_name: " + directory + "\nitem_name: " + filename[0] + "\n---"
                with open(path, 'w') as f:
                    f.write(index_content)
                    print("Item file " , path,  " Created ")
            else:    
                print("Item file " , path ,  " already exists")  

            


