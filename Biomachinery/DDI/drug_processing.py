import csv
import json

csv_file_path = 'data/drug_selection.csv'
with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.reader(csv_file_handler)

    result_dict = dict({'results':[]})
    for row in csv_reader:
        drug = row[0]
        entry = dict()
        entry['id'] = drug
        entry['text'] = drug
        result_dict['results'].append(entry)

with open("data/drugs.json", "w") as outfile:
    json.dump(result_dict, outfile)
