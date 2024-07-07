##### README #####
# author: Tovarlogic@gmail.com
# use this scripts to maintain files up-to-date.
# execute it before building locally or pushing to gitHub

###### TO-DOs #######
# añadir page_sequence a cada promesa
# añadir a cada promesa todo el contenido nuevo de TOPICS

import os
import shutil
import yaml
import uuid
from termcolor import colored

# MAIN PATHS
app_path = os.path.abspath('..')
data_path = app_path + '/_data/'

## DATA PATHS
documents_path = data_path + 'documents/'
tracks_path = data_path + 'tracks/'
categorization_path = data_path + 'categorization/'

## DATA GENERATED BY THIS SCRIPT
statements_path = data_path + 'statements/'
topics_path = data_path + 'topics/'

## COLLECTIONS PATHS
docs_pages_path = app_path + '/_docs/'
tracks_pages_path = app_path + '/_tracks/'
statements_pages_path = app_path + '/_statements/'
topics_pages_path = app_path + '/_topics/'

def writeStatement(statement):
    if not os.path.exists(statements_path):
        os.mkdir(statements_path)
    
    file_path = statements_path + statement['id'] + '.yaml'
    if not os.path.exists(file_path):
        with open(file_path, 'w') as df:
            yaml.dump(statement, df, allow_unicode=True, sort_keys=False, width=float("inf"))

def saveStatement(item, type, doc_metadata, parent_categories = False, parent_topics = False, parent_statement = False, parent_chapter = False):
    statement = {}

    statement['id'] = item['id']
    statement['type'] = type

    for data in doc_metadata:
        statement[data] = doc_metadata[data] 
    
    if 'page' in item:
        statement['page'] = item['page']
    
    if parent_statement:
        statement['parent_statement'] = parent_statement
    
    if parent_chapter:
        statement['parent_chapter'] = parent_chapter

    if 'children' in item:
        extractStatements(item['children'], doc_metadata, parent_categories, parent_topics, item['id'], parent_chapter)

        statement['children_promises'] = []
        statement['children_statements'] = []

        for children in item['children']:
            if 'promise' in children:
                statement['children_promises'].append(children['promise']['id'])
            if 'statement' in children:
                statement['children_statements'].append(children['statement']['id'])

    if 'title' in item:
        statement['title'] = item['title']
    
    if 'text' in item:
        statement['text'] = item['text']

    if 'categories' in item:
        statement['categories'] = item['categories']
        parent_categories = item['categories']
    elif parent_categories: # inherited categories
        statement['categories'] = parent_categories

    if 'topics' in item:
        statement['topics'] = item['topics']
        parent_topics = item['topics']
    elif parent_topics: # inherited topics
        statement['topics'] = parent_topics
    
    if 'analysis' in item:
        statement['analysis'] = item['analysis']

    writeStatement(statement)    

def saveTopics(item, doc_metadata):
    # topics are not inherited so only process if the statement contains a topic label
    if 'topics' in item:
        if isinstance(item['topics'], str):
            item['topics'] = [item['topics']]
        for topic in item['topics']:
            if 'name' in topic:
                name = topic['name']
                name_slug = name.lower().replace(' ', '-')
            else:
                name = topic
                name_slug = name.lower().replace(' ', '-')

            doc = {}
            doc['name'] = name 

            statements = {}
            
            parties = []

            if isinstance(doc_metadata['parties'], str): 
                doc_metadata['parties'] = [doc_metadata['parties']]
            parties.extend(doc_metadata['parties'])

            # check if there is already a topic file in place
            # if so, load existing topic data
            file_path = topics_path + name_slug + '.yaml'
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    doc = yaml.safe_load(f)
            else:
                with open(file_path, 'w') as f:
                    doc['statements_count'] = 0
                    yaml.dump(doc, f, allow_unicode=True) 
                    print("Topic " , name,  colored(" Created", 'cyan'))

            # load this statement
            if not 'statements' in doc:
                doc['statements'] = []

            if not 'position_positive' in doc:
                doc['position_positive'] = []
                doc['position_positive_count'] = 0

            if not 'position_negative' in doc:
                doc['position_negative'] = []
                doc['position_negative_count'] = 0

            if not 'status_quo_positive' in doc:
                doc['status_quo_positive'] = []
                doc['status_quo_positive_count'] = 0

            if not 'status_quo_negative' in doc:
                doc['status_quo_negative'] = []
                doc['status_quo_negative_count'] = 0
            
            if not 'proposed_actions' in doc:
                doc['proposed_actions'] = []
                doc['proposed_actions_count'] = 0
            
            if not 'other' in doc:
                doc['other'] = []
                doc['other_count'] = 0

            new = { }
            new['id'] = item['id']
            new['parties'] = doc_metadata['parties']

            doc['statements'].append(new)
            doc['statements_count'] = doc['statements_count'] + 1

            if 'position_positive' in topic:
                doc['position_positive'].append(new)
                doc['position_positive_count'] = doc['position_positive_count'] + 1
            
            if 'position_negative' in topic:
                doc['position_negative'].append(new)
                doc['position_negative_count'] = doc['position_negative_count'] + 1

            if 'status_quo_positive' in topic:
                doc['status_quo_positive'].append(new)
                doc['status_quo_positive_count'] = doc['status_quo_positive_count'] + 1

            if 'status_quo_negative' in topic:
                doc['status_quo_negative'].append(new)
                doc['status_quo_negative_count'] = doc['status_quo_negative_count'] + 1
            
            if 'proposed_actions' in topic:
                doc['proposed_actions'].append(new)
                doc['proposed_actions_count'] = doc['proposed_actions_count'] + 1
            
            if not 'position_positive' in topic:
                if not 'position_negative' in topic:
                    if not 'status_quo_positive' in topic:
                        if not 'status_quo_negative' in topic:
                            if not 'proposed_actions' in topic:
                                doc['other'].append(new)
                                doc['other_count'] = doc['other_count'] + 1

            #erase file content and rewrite
            open(file_path, 'w').close()
            with open(file_path, 'w') as f:
                yaml.dump(doc, f, allow_unicode=True)
                print("Topic " , name,  colored(" edited", 'yellow'))
                                           
def extractStatements(content, doc_metadata, categories = False, topics = False, parent_statement = False, parent_chapter = False):
    for item in content:
        for i in item:
            if i =='statement':
                saveStatement(item['statement'], 'statement', doc_metadata, categories, topics, parent_statement, parent_chapter)
                saveTopics(item['statement'], doc_metadata)
            elif i =='promise':
                saveStatement(item['promise'], 'promise', doc_metadata, categories, topics, parent_statement, parent_chapter)
                saveTopics(item['promise'], doc_metadata)
            elif i == 'chapter':
                if 'id' in item['chapter']:
                    parent_chapter = item['chapter']['id']

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
                    extractStatements(item['chapter']['children'], doc_metadata, parent_categories, parent_topics, False, parent_chapter)

def process_documents():
    # this function is used to extract all statements from every document in "_data/documents/" 
    # and save each in a single yaml file in _data/statements/
    # as well as each single topic file in _data/topics/
    # Each promise content is copied along with metadada such as "categories" and "promises". 
    # If the promise does not have declared them, may be inherited from parent "promises" or "chapters"
    # yaml "content" and "children" are lists; the rest are dicts

    # remove generated pages and data
    print(" ----------- REMOVING AUTOGENERATED FILES------------")
    if os.path.exists(statements_path):
        shutil.rmtree(statements_path)
        print("All Statements",  colored(" deleted", 'red'))
    os.mkdir(statements_path)
    if os.path.exists(topics_path):
        shutil.rmtree(topics_path)
        print("All Topics",  colored(" deleted", 'red'))
    os.mkdir(topics_path)

    print(" ----------- PROCESANDO DOCUMENTOS ------------")
    print(documents_path)
    # get all documents
    (_, _ , files) = next(os.walk(documents_path))

    for file in files:
        doc_metadata = {}
        print("-->",file)
        with open(documents_path + file, 'r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
            doc_metadata['parent_document'] = doc['id']
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
    if os.path.exists(docs_pages_path):
        shutil.rmtree(docs_pages_path)

    if not os.path.exists(docs_pages_path):
        os.makedirs(docs_pages_path)

    # get all data files
    (_, _ , files) = next(os.walk(documents_path))

    for item in files: 
        views = ["statements-promises", "promises"]
        for view in views:    
            f = open(documents_path + "/" + item, "r")
            data = f.readline().strip('\n')
            f.close() 
            data = data.split(": ")
            id = data[1]
            filename = item.split(".")
            if view == 'statements-promises':
                view_name = ""
            else:
                view_name = '_' + view      
            # create item page
            path = docs_pages_path + filename[0] + view_name + '.md'
            if not os.path.exists(path) and id:
                index_content = "---\nuid: " + id + "\ndoc_name: " + filename[0] + "\n---"
                with open(path, 'w') as f:
                    f.write(index_content)
                    print("Item file " , path,  colored(" Created", 'cyan'))

def create_track_pages():
    # use this function to create every "track page" from the _data/tracks/ files

    print(" ----------- GENERANDO PÁGINAS: TRACKs ------------")

    if os.path.exists(tracks_pages_path):
        shutil.rmtree(tracks_pages_path)

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
        
        # create tracker index page  
        path = track_path + '/index.md'
        if not os.path.exists(path):
            index_content = "---\ntrack_name: " + filename[0] + "\nlayout: track" + "\nslug: " + filename[0] + "-index" + "\n---"
            with open(path, 'w') as f:
                f.write(index_content)
            print("Index file " , path,  colored(" Created", 'cyan'))

def create_statement_pages():
    if os.path.exists(statements_pages_path):
        shutil.rmtree(statements_pages_path)

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

def create_topics_pages():
    print(" ----------- GENERANDO PÁGINAS: TOPICS ------------")

    if os.path.exists(topics_pages_path):
        shutil.rmtree(topics_pages_path)

    if not os.path.exists(topics_pages_path):
        os.makedirs(topics_pages_path)

    # get all topics data files
    (_, _ , files) = next(os.walk(topics_path))

    for item in files:     
        f = open(topics_path + item, "r")
        data = yaml.safe_load(f)
        f.close() 
        filename = item.split(".")
                
        # create item page
        path = topics_pages_path + filename[0] + '.md'
        if not os.path.exists(path):
            content = "---\ntopic_name: " + data['name'] + "\n---"
            with open(path, 'w') as f:
                f.write(content)
                print("Item file " , path,  colored(" Created", 'cyan'))

def process_categorization():
    # use this function to create and populate a categorization file for unique (no duplicates) 
    # "parent goals", "goals", "objectives", "topics", and "categories" extracted from all statements
    # is useful to detect typos and to have bigger picture of the data

    # TO-DO: Rehacer al completo para mostrar los topics que no se encuentren en topics.yaml
    print(" ----------- REVISANDO CATEGORIZACIÓN ------------")
    print(categorization_path)
    print(topics_path)

    # get all statement files
    (_, _ , files) = next(os.walk(statements_path))

    topics_input_path = categorization_path + 'topics.yaml'
    destination_path = categorization_path + 'topics_not_listed.yaml'

    print("Check for new or not listed topics in " + destination_path)

    #Reset destination file:
    if os.path.exists(destination_path):
        os.remove(destination_path)

    content = "parent_goals:\n" + "goals:\n" + "objectives:\n" + "topics:\n" + "categories:\n"
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
        
        if destination_file['topics'] is not None:
            topics = set(destination_file['topics'])
        else:
            topics = set()
        
        if destination_file['categories'] is not None:
            categories = set(destination_file['categories'])
        else:
            categories = set()

    # collect goals and objectives from statements
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
                    for topic in promise_file['topics']:
                        topics.update(topic)
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
#create_statement_pages() # DEPRECATED: for faster building time now using AJAX with a single /statements/show page
#create_topics_pages() # DEPRECATED: for faster building time now using AJAX with a single /topics/show page
#process_categorization() # not working properly yet

print("FINALIZACIÓN ", "[", colored("ÉXITO", 'green'), "]")