import json
import yaml
import sys

in_file = sys.argv[1]
out_file = in_file.split('.')[0] + ".json"

with open(in_file, 'r') as yaml_in, open(out_file, "w") as json_out:
    yaml_playload = yaml.safe_load(yaml_in) 
    json.dump(yaml_object, json_out)