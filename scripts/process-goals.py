##### README #####
# author: Tovarlogic@gmail.com
# use this script to create and populate a categorization file for unique (no duplicates) "parent goals", "goals", "objectives", "topics", and "categories" extracted from all promises

import os
import yaml

# PATHS
app_path = os.path.abspath('..')
data_path = app_path + '/_data/promises/'
destination_path = app_path + '/_data/categorization/promises.yaml'

# get all promises files
(_, _ , files) = next(os.walk(data_path))

#Reset destination file:
if os.path.exists(destination_path):
    os.remove(destination_path)
    print("File " + destination_path + " deleted")

content = "parent_goals:\n" + "goals:\n" + "objectives:\n" + "topics:\n" + "categories:\n"
with open(destination_path, 'w') as f:
    f.write(content)
    print("File " + destination_path + " created")


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
    
    if destination_file['topics'] is not None:
        topics = set(destination_file['topics'])
    else:
        topics = set()
    
    if destination_file['categories'] is not None:
        categories = set(destination_file['categories'])
    else:
        categories = set()

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
        
        try:
            if promise_file['topics']:
                topics.update(promise_file['topics'])
        except KeyError:
            pass
        
        try:
            if promise_file['categories']:
                categories.update(promise_file['categories'])
        except KeyError:
            pass

#overwrite the destination file
output = {'parent_goals': list(parent_goals), 'goals': list(goals), 'objectives': list(objectives), 'topics': list(topics), 'categories': list(categories)}
with open(destination_path, 'w') as f:
    yaml.dump(output, f, allow_unicode=True)
    print("File " + destination_path + " populated")

