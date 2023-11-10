##### README #####
# author: Tovarlogic@gmail.com
# use this scripts to maintain files up-to-date.
# execute it before building locally or pushing to gitHub

import os
import shutil
import yaml
import uuid
from termcolor import colored

# PATHS
app_path = os.path.abspath('..')
data_path = app_path + '/_data/'

## DATA PATHS
documents_path = data_path + 'documents/'
statements_path = data_path + 'statements/'
tracks_path = data_path + 'tracks/'
categorization_path = data_path + 'categorization/'

## COLLECTIONS PATHS
docs_pages_path = app_path + '/_docs/'
tracks_pages_path = app_path + '/_tracks/'
statements_pages_path = app_path + '/_statements/'


def writeStatement(statement):
    if not os.path.exists(statements_path):
        os.mkdir(statements_path)
    
    file_path = statements_path + statement['id'] + '.yaml'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as df:
            yaml.dump(statement, df, allow_unicode=True, sort_keys=False, width=float("inf"))

def saveStatement(item, type, doc_metadata, parent_categories = False, parent_topics = False, parent_id = False):
    statement = {}

    statement['id'] = item['id']
    statement['type'] = type
    if parent_id:
        statement['parent_statement'] = parent_id

    for data in doc_metadata:
        statement[data] = doc_metadata[data] 
    
    if 'page' in item:
        statement['page'] = item['page']

    if 'categories' in item:
        statement['categories'] = item['categories']
        parent_categories = item['categories']
        if 'topics' in item:
            statement['topics'] = item['topics']
            parent_topics = item['topics']
    elif parent_categories: # inherited categories
        statement['categories'] = parent_categories
        if 'topics' in item:
            statement['topics'] = item['topics']
            parent_topics = item['topics']
        elif parent_topics: # inherited topics, only if no new categories
            statement['topics'] = parent_topics
    
    if 'title' in item:
        statement['title'] = item['title']
    
    if 'text' in item:
        statement['text'] = item['text']
    
    if 'children' in item:
        extractStatements(item['children'], doc_metadata, parent_categories, parent_topics, item['id'])
        statement['has_children'] = True

    writeStatement(statement)    
    
def extractStatements(content, doc_metadata, categories = False, topics = False, parent_id = False):
    for item in content:
        for i in item:
            if i =='declaration':
                saveStatement(item['declaration'], 'declaration', doc_metadata, categories, topics, parent_id)
            elif i =='promise':
                saveStatement(item['promise'], 'promise', doc_metadata, categories, topics, parent_id)
            elif i == 'chapter':
                if 'categories' in item['chapter']:
                    parent_categories = item['chapter']['categories']
                    if 'topics' in item['chapter']:
                        parent_topics = item['chapter']['topics']
                    else:
                        parent_topics = False #if new categories, then topics can not be inherited
                else: 
                    parent_categories = categories
                    if 'topics' in item['chapter']:
                        parent_topics = item['chapter']['topics']
                    else:
                        parent_topics = topics
                
                if 'children' in item['chapter']:
                    extractStatements(item['chapter']['children'], doc_metadata, parent_categories, parent_topics)

def process_documents():
    # this script is used to extract all statements from every document in "_data/documents/" 
    # and save each in a single yaml file in _data/statements/
    # Each promise content is copied along with metadada such as "categories" and "promises". 
    # If the promise does not have declared them, may be inherited from parent "promises" or "chapters"
    # yaml "content" and "children" are lists; the rest are dicts

    print(" ----------- PROCESANDO DOCUMEMTOS ------------")

    # get all documents
    (_, _ , files) = next(os.walk(documents_path))

    for file in files:
        doc_metadata = {}
        print("-->",file)
        with open(documents_path + file, 'r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
            doc_metadata['doc_id'] = doc['id']
            doc_metadata['parties'] = doc['parties']

            if 'scope' in doc:
                doc_metadata['scope'] = doc['scope']
            
            if 'country' in doc:
                doc_metadata['country'] = doc['country']
            
            if 'organization' in doc:
                doc_metadata['organization'] = doc['organization']
            
            if 'region' in doc:
                doc_metadata['region'] = doc['region']
            
            if 'locality' in doc:
                doc_metadata['locality'] = doc['locality']

            if 'election_type' in doc:
                doc_metadata['election_type'] = doc['election_type']

            if 'election_date' in doc:
                doc_metadata['election_date'] = doc['election_date']
            
            if 'publication_date' in doc:
                doc_metadata['publication_date'] = doc['publication_date']

            extractStatements(doc['content'], doc_metadata)

def create_doc_pages():
    # use this script to create every "docs page" related to _data/documents   

    print(" ----------- GENERANDO PÁGINAS: DOCs ------------")

    if not os.path.exists(docs_pages_path):
        os.makedirs(docs_pages_path)

    # get all data files
    (_, _ , files) = next(os.walk(documents_path))

    for item in files:     
        f = open(documents_path + "/" + item, "r")
        data = f.readline().strip('\n')
        f.close() 
        data = data.split(": ")
        id = data[1]
        filename = item.split(".")
                
        # create item page
        path = docs_pages_path + filename[0] + '.md'
        if not os.path.exists(path) and id:
            index_content = "---\nuid: " + id + "\ndoc_name: " + filename[0] + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
                print("Item file " , path,  colored(" Created", 'cyan'))

def create_track_pages():
    # use this script to create every "track page" from the _data/tracks/ files

    print(" ----------- GENERANDO PÁGINAS: TRACKs ------------")

    if not os.path.exists(tracks_pages_path):
        os.makedirs(tracks_pages_path)

    # get all data files
    (_, _ , files) = next(os.walk(tracks_path))

    for file in files:
        # create track directory
        filename = file.split(".")
        track_path = tracks_pages_path + filename[0]

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

def create_statement_pages():
    if not os.path.exists(statements_pages_path):
        os.makedirs(statements_pages_path)

    # get all data files
    (_, _ , files) = next(os.walk(statements_path))

    for item in files:     
        f = open(statements_path + item, "r")
        data = f.readline().strip('\n')
        f.close() 
        data = data.split(": ")
        id = data[1]
        filename = item.split(".")
                
        # create item page
        path = statements_pages_path + filename[0] + '.md'
        if not os.path.exists(path):
            index_content = "---\nuid: " + id + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
                print("Item file " , path,  colored(" Created", 'cyan'))

def process_categorization():
    # use this script to create and populate a categorization file for unique (no duplicates) 
    # "parent goals", "goals", "objectives", "topics", and "categories" extracted from all statements
    # is useful to detect typos and to have bigger picture of the data

    print(" ----------- PROCESANDO CATEGORIZACIÓN ------------")

    # get all promises files
    (_, _ , files) = next(os.walk(statements_path))

    destination_path = categorization_path + 'all_data.yaml'
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
        with  open(statements_path + "/" + item, 'r', encoding='utf-8') as f:
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

process_documents()
create_track_pages()
create_doc_pages()
create_statement_pages()
process_categorization()