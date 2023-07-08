##### README #####
# author: Tovarlogic@gmail.com
# use this script to create every track page from the _data files before building jekyll

import os
import yaml
from termcolor import colored

# PATHS
data_path = os.getcwd() + '/_data/promises/'
destination_path = os.getcwd() + '/_promises/'

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
        path = destination_path + '/' + id + '.md'
        if not os.path.exists(path) and id:
            index_content = "---\nuid: " + id + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
                print("Item file " , path,  colored(" Created", 'cyan'))
        else:    
            print("Item file " , path ,  colored(" already exists", 'green'))  
