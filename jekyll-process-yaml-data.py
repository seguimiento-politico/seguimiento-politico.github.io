##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import yaml

# PATHS
data_path = os.getcwd() + '/_data'
trackers_path = data_path + '/tracks/trackers/'
items_path = data_path + '/tracks/items/'

tracks_path = os.getcwd() + '/tracks/'

# get all directories
(_, directories , _) = next(os.walk(trackers_path))

for directory in directories:
    (_, _, trackers) = next(os.walk(trackers_path + directory))

    tracker_path = tracks_path + directory

    if not os.path.exists(tracker_path):
        os.makedirs(tracker_path)
        print("Directory " , tracker_path,  " Created ")
    else:    
        print("Directory " , tracker_path ,  " already exists")

    for track in trackers:
        # create tracks subfolders
        dirname = track.split(".")
        track_path = tracker_path + '/' + dirname[0]
        if not os.path.exists(track_path):
            os.makedirs(track_path)
            print("Subfolder " , track_path,  " Created ")
        else:    
            print("Subfolder " , track_path ,  " already exists")  
        
        # create tracker index page  
        path = track_path + '/index.md'
        if not os.path.exists(path):
            index_content = "---\nsubfolder: " + directory + "\ntrack_name: " + dirname[0] + "\nlayout: track\n---"
            with open(path, 'w') as f:
                f.write(index_content)
            print("Index file " , path,  " Created ")
        else:    
            print("Index file " , path ,  " already exists")  
        
        # get track items
        items_dir = items_path + directory + '/' + dirname[0]
        
        if os.path.exists(items_dir):
            (_, _, items) = next(os.walk(items_dir))

            for item in items:
                filename = item.split(".")
                # create item file
                path = track_path + '/' + filename[0] + '.md'
                if not os.path.exists(path):
                    index_content = "---\nsubfolder: " + directory + "\ntrack_name: " + dirname[0] + "\nitem_name: " + filename[0] + "\n---"
                    with open(path, 'w') as f:
                        f.write(index_content)
                    print("Item file " , path,  " Created ")
                else:    
                    print("Item file " , path ,  " already exists")  


