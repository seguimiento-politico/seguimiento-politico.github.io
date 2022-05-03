# This script formats a YAML file of "diputados del congreso" 
# to the structure used in "Seguimiento Político"
# The data source is a json file from https://www.congreso.es/busqueda-de-diputados?statusOpendata=true

import yaml
import sys

in_file = sys.argv[1]
out_file = in_file.split('.')[0] + "_formatted.yaml"

with open(in_file, 'r') as fi, open(out_file, 'w') as fo:
    data = yaml.safe_load(fi)

    for item in data:
        del item['FechaAlta']
        del item['FechaBaja']
        del item['GrupoParlamentario']
        del item['Biografia']
        del item['FechaCondicionPlena']
        del item['Estado']
        del item['Legislatura']

        value = item['Circunscripcion'].split('/')
        item['electorate'] = value[0]
        del item['Circunscripcion']

        item['party'] = item['Formacion']
        del item['Formacion']

        value = item['Nombre'].split(', ')
        item['name'] = value[1] + " " + value[0]
        del item['Nombre']

    yaml.safe_dump(data, fo, encoding='utf-8', allow_unicode=True, sort_keys=False)

