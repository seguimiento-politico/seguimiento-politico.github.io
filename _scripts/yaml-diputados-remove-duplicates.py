# This script removes all duplicates of a yaml file and save results in a new file
import yaml
import sys

#input_files = ['diputados19-23_formatted.yaml', 'diputados16-19_formatted.yaml', 'diputados11-16_formatted.yaml', 'diputados08-11_formatted.yaml', 'diputados04-08_formatted.yaml', 'diputados00-04_formatted.yaml', 'diputados96-00_formatted.yaml', 'diputados93-96_formatted.yaml', 'diputados89-93_formatted.yaml', 'diputados86-89_formatted.yaml', 'diputados82-86_formatted.yaml', 'diputados79-82_formatted.yaml', 'diputados77-79_formatted.yaml']
input_files = ['diputados77-23_merged.yaml']

for fi in input_files: 
    out_file = fi.split('.')[0]+'_no_duplicates.yaml'
    y = 0
    x = 0
    with open(fi, 'r') as f1:
        data = yaml.safe_load(f1)

    for item1 in data:
        if item1:
            i = 0
            for item2 in data:
                if item2:
                    if item1['name'] == item2['name'] and item1['party'] == item2['party']:
                        i += 1
                        if i > 1:
                            del item2['name']
                            del item2['party']
                            del item2['electorate']
                            y += 1
                            if i == 2:
                                x += 1
                                print ('Duplicate: ' + item1['name']+':'+ item1['party']) 

    with open(out_file, 'w') as fo:
        yaml.safe_dump(data, fo, encoding='utf-8', allow_unicode=True)

    a_file = open(out_file, "r")
    lines = a_file.readlines()
    a_file.close()

    new_file = open(out_file, "w")

    for line in lines:
        if line.strip("\n") != "- {}":
            new_file.write(line)
    new_file.close()

    print ('Diputados repetidos: ') 
    print(x)
    print ('Total repeticiones: ') 
    print(y)
    print ('Total lines removed: ') 
    print(y*2)

