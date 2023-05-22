import json

def put_data(textfile, data): #requires import json

    result = []
    for record in data:
        entry = dict()
        entry['Drug 1'] = str(record[0]) #str
        entry['Drug 2'] = str(record[1]) #str
        entry['Side Effect'] = str(record[2]) #str
        entry['Confidence'] = float(record[3]) #float
        result.append(entry)

    with open(textfile, "w") as outfile:
        json.dump(result, outfile)
