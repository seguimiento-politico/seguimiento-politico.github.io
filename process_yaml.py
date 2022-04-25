##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import yaml

# PATHS
data_path = os.getcwd() + '/_data'
trackers_path = data_path + '/trackers'
promises_path = data_path + '/track_items'

tracks_path = os.getcwd() + '/tracks'

# get all trackers
(_, _, trackers) = next(os.walk(trackers_path))

for track in trackers:
    # create tracks subfolders
    dirname = track.split(".")
    path = tracks_path + '/' + dirname[0]
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory " , path,  " Created ")
    else:    
        print("Directory " , path ,  " already exists")  
    
    # create tracker index page  
    path = path + '/index.md'
    if not os.path.exists(path):
        index_content = "---\ntrack_name: " + dirname[0] + "\nlayout: track\n---"
        with open(path, 'w') as f:
            f.write(index_content)
        print("File " , path,  " Created ")
    else:    
        print("File " , path ,  " already exists")  
    
    # get track promises
    promises_dir = promises_path + '/' + dirname[0]
    (_, _, promises) = next(os.walk(promises_dir))

    for promise in promises:
        filename = promise.split(".")
        # create promise file
        path = tracks_path + '/' + dirname[0] + '/' + filename[0] + '.md'
        if not os.path.exists(path):
            index_content = "---\ntrack_name: " + dirname[0] + "\nitem_name: " + filename[0] + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
            print("File " , path,  " Created ")
        else:    
            print("File " , path ,  " already exists")  


