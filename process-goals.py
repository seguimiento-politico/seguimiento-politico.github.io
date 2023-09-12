##### README #####
# author: Tovarlogic@gmail.com
# use this script to create populate a categorization file for unique (no duplicates) "parent goals", "goals" and "objectives" extracted from all promises

import os
import yaml
from termcolor import colored

# PATHS
data_path = os.getcwd() + '/_data/promises/'
destination_path = os.getcwd() + '/_data/categorization/promises_goals.yaml'

# get all files
(_, _ , files) = next(os.walk(data_path))

#check if destination file exists. create it if it does not:
if not os.path.exists(destination_path):
    content = "parent_goals:\n" + "goals:\n" + "objectives:\n"
    with open(destination_path, 'w') as f:
        f.write(content)

#set output variables
output = {}
with open(destination_path, 'r', encoding='utf-8') as f:
    destination_file = yaml.safe_load(f)
    if destination_file['parent_goals'] is not None:
        parent_goals = set(destination_file['parent_goals'])
    else:
        parent_goals = set()

    if destination_file['goals'] is not None:
        goals = set(destination_file['goals'])
    else:
        goals = set()

    if destination_file['objectives'] is not None:
        objectives = set(destination_file['objectives'])
    else:
        objectives = set()

# collect goals and objectives from promises
for item in files:   
    with  open(data_path + "/" + item, 'r', encoding='utf-8') as f:
        promise_file = yaml.safe_load(f)
        try:
            if promise_file['parent_goals']:
                parent_goals.update(promise_file['parent_goals'])
        except KeyError:
            pass
        
        try:
            if promise_file['goals']:
                goals.update(promise_file['goals'])
        except KeyError:
            pass
        
        try:
            if promise_file['objectives']:
                objectives.update(promise_file['objectives'])
        except KeyError:
            pass

#overwrite the destination file
output = {'parent_goals': list(parent_goals), 'goals': list(goals), 'objectives': list(objectives)}
print(output)
with open(destination_path, 'w') as f:
    yaml.dump(output, f, allow_unicode=True)

