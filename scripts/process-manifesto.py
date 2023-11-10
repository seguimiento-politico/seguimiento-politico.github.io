##### README #####
# author: Tovarlogic@gmail.com
# DEPRECATED
# this script is used to convert manifestos documents in yaml format (version 1) into the new format which includes every promise.

import os
import shutil
import yaml
import uuid
from termcolor import colored

# PATHS
app_path = os.path.abspath('..')
promises_path = app_path + '/_data/test_promises/'
manifestos_path = app_path + '/_data/test_docs/'
destination_path = app_path + '/_data/docs/'

chapters = []
promises_cont = 0
chapter_promises_cont = 0
files_cont = 0

def myFunc(e):
  return e['ref_section']
  
def get_promises(chapter):    
    list = []
    for promise in promises: 
        processed = False
        if os.path.exists(promises_path + "/" + promise):
            with open(promises_path + "/" + promise, 'r', encoding='utf-8') as promise_file: 
                global files_cont
                files_cont += 1
                p = yaml.safe_load(promise_file)
                #check if promise corresponds to the same manifesto
                if m['id'] == p['doc_id']:
                    if 'ref_parent_chapter' in p:
                        chapter_string = ""
                        cont = 0
                        for x in chapter:
                            if cont > 0:
                                chapter_string += "."    
                            chapter_string += str(x) 
                            cont += 1
                        #check if promise corresponds to the same chapter
                        if p['ref_parent_chapter'] == chapter_string:
                            processed = True
                            global promises_cont 
                            promises_cont += 1
                            global chapter_promises_cont 
                            chapter_promises_cont += 1
                            print("\rpromesa", chapter_promises_cont, end=" ")
                            proposition = {}
                            proposition['id'] = p['id']
                            proposition['proposition'] = p['title']
                            if 'page' in p:
                                proposition['page'] = p['page']
                            if 'ref_section' in p:
                                proposition['ref_section'] = p['ref_section']
                            else:
                                proposition['ref_section'] = ""
                            # set promise content
                            proposition['children'] = []
                            part = {}
                            if 'description' in p:
                                part['id'] = str(uuid.uuid4())
                                part['declaration'] = p['description']
                                proposition['children'].append(part)
                                part = {}
                            partial = False
                            quote = ""

                            for statement in p['statements']: 
                                if 'partial' in statement:
                                    if statement['partial'] == 'ini':
                                        partial = True
                                        quote = statement['quote']
                                    elif statement['partial'] == 'end':
                                        quote += " " + statement['quote']
                                        partial = False
                                else:
                                    if partial == True: 
                                        quote += " " + statement['quote']
                                    else:
                                        quote = statement['quote']
                                
                                if partial == False:
                                    # set promise metadata
                                    part['id'] = str(uuid.uuid4())
                                    part['promise'] = quote
                                    
                                    proposition['children'].append(part)
                                    part = {}

                            #monitor possible error
                            if partial == True:
                                print(colored("Error de formato: ", 'red'), proposition)
                            
                            list.append(proposition) 
                            #order promises        
                            list.sort(key=myFunc)
            # to speed up, remove promise file if already processed                 
            if processed == True: 
                os.remove(promises_path + "/" + promise) 

    return list

def go_deeper(dict):
    list = []

    for item in dict:
        part = {}
        if 'chapter' in item:
            part['chapter'] = item['chapter']

            #register current chart and subcharts
            chapters.append(item['chapter'])
        if 'title' in item:
            part['title'] = item['title']

        if 'page' in item:
            part['page'] = item['page']

        if 'description' in item:
            text = item['description'].replace('\r\n', '')
            part['children'] = []
            part['children'].append({'id': str(uuid.uuid4()), 'declaration': text})

        if 'children' in item:
            if not 'children' in part:
                part['children'] = []

            result = go_deeper(item['children'])
            for item in result:
                part['children'].append(item)
        print(chapters)
        global chapter_promises_cont 
        chapter_promises_cont = 0
        propositions = get_promises(chapters)
        for item in propositions:
            if not 'children' in part:
                part['children'] = []
            part['children'].append(item)

        list.append(part)

        # remove last subchapter
        chapters.pop()

    return list

def create_metadata(m, dict):
    # set manifesto metadata
    dict['id'] = m['id']

    if 'version' in m:
        dict['version'] = m['version']
    if 'type' in m:  
        dict['type'] = m['type']
    if 'parties' in m:
        dict['parties'] = m['parties']
    if 'election_type' in m:
        dict['election_type'] = m['election_type']
    if 'election_date' in m:
        dict['election_date'] = m['election_date']
    if 'url' in m:
        dict['url'] = m['url']
    if 'web_history' in m:
        dict['web_history'] = m['web_history']
    if 'title' in m:
        dict['title'] = m['title']
    if 'description' in m:
        dict['description'] = m['description'].replace('\n', '')
    
    return dict

def create_yaml(m):
    dict = create_metadata(m, {}) 
    dict['index'] = {}
    result = go_deeper(m['index'])
    if result:
        dict['index'] = result

    return dict

#reset destination folder
if os.path.exists(destination_path):
    try:
        shutil.rmtree(destination_path)
        print("Directory removed successfully")
    except OSError as o:
        print(f"Error, {o.strerror}: {destination_path}")

os.mkdir(destination_path)
#shutil.copytree(manifestos_path, destination_path)

print("Carpeta " , destination_path,  colored(" Reseteada", 'green'))

# get all files
(_, _ , promises) = next(os.walk(promises_path))
(_, _ , manifestos) = next(os.walk(manifestos_path))

for doc in manifestos:  
    with open(manifestos_path + doc, 'r', encoding='utf-8') as manifest_file:  
        print("Procesando " , doc)
        m = yaml.safe_load(manifest_file)
        yaml_manifesto = create_yaml(m)
        with open(destination_path + doc, 'w', encoding='utf-8') as df:  
            #yaml.dump(yaml_manifesto, df)      
            yaml.dump(yaml_manifesto, df, allow_unicode=True, sort_keys=False, width=float("inf"))

        print("\r" , doc, colored("[", 'green'), colored(promises_cont, 'green'), colored("]", 'green'))
                            


                                
                                 
                                    
        
        