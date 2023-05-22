import json

def get_data(textfile):

    with open(textfile, 'r') as file:
        lines = file.readlines()

    drug_list = []

    if lines!=[]:
        
        input_data = list(map(eval, lines[0].strip().split()))
        drug_list = list(input_data[0])

    return drug_list



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


data = [
    ['drug1','drug2','melanoma','0.85'],
    ['drug2','drug4','yellow fever','0.6'],
    ['drug1','drug3','liver damage','0.33']
    ]

put_data('output_file.json', data)
