##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import shutil
import yaml
from termcolor import colored
import uuid

# PATHS# PATHS
app_path = os.path.abspath('..')
data_path = app_path + './_data/promises/'
destination_path = app_path + './_data/promises_analysis/'

# get all files
(_, _ , files) = next(os.walk(data_path))

        
for item in files:     
    if item != "settings.yaml" and item != "politicians.json":
        f = open(data_path + "/" + item, "r")
        data = f.readline().strip('\n')
        f.close() 
        data = data.split(": ")
        id = data[1]
        filename = item.split(".")
                
        # create item page
        path = destination_path + '/' + filename[0] + '.yaml'
        uuid4 = uuid.uuid4()
        if not os.path.exists(path) and id:
            index_content = "id: " + str(uuid4) + "\n" + "promise_id: " + id
            with open(path, 'w') as f:
                f.write(index_content)
                print("Item file " , path,  colored(" Created", 'cyan'))
        else:    
            print("Item file " , path ,  colored(" already exists", 'green'))  
