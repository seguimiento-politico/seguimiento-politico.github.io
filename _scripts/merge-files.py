# This script merges many files into a new one. is format agnostic
#input_files = ['diputados19-23_formatted.yaml', 'diputados16-19_formatted.yaml', 'diputados11-16_formatted.yaml', 'diputados08-11_formatted.yaml', 'diputados04-08_formatted.yaml', 'diputados00-04_formatted.yaml', 'diputados96-00_formatted.yaml', 'diputados93-96_formatted.yaml', 'diputados89-93_formatted.yaml', 'diputados86-89_formatted.yaml', 'diputados82-86_formatted.yaml', 'diputados79-82_formatted.yaml', 'diputados77-79_formatted.yaml']
input_files = ['diputados19-23_formatted_no_duplicates.yaml', 'diputados16-19_formatted_no_duplicates.yaml', 'diputados11-16_formatted_no_duplicates.yaml', 'diputados08-11_formatted_no_duplicates.yaml', 'diputados04-08_formatted_no_duplicates.yaml', 'diputados00-04_formatted_no_duplicates.yaml', 'diputados96-00_formatted_no_duplicates.yaml', 'diputados93-96_formatted_no_duplicates.yaml', 'diputados89-93_formatted_no_duplicates.yaml', 'diputados86-89_formatted_no_duplicates.yaml', 'diputados82-86_formatted_no_duplicates.yaml', 'diputados79-82_formatted_no_duplicates.yaml', 'diputados77-79_formatted_no_duplicates.yaml']
output_file = 'diputados77-23_merged.yaml'

data = ""
i = 0
for fi in input_files:
    i+=1
    if i == 1:
        with open(fi, 'r') as f:
            data = f.read()
            data += "\n"

        with open(output_file, 'w') as fo:
            fo.write(data)
        
    else:
        with open(fi, 'r') as f2:
            data = f2.read()
            data += "\n"
        
        with open(output_file, 'a') as fo:
            fo.write(data)

    