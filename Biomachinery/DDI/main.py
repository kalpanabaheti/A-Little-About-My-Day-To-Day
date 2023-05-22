import time
import csv
import driver
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/process', methods=['POST', 'GET'])
def process_calculation():
  if request.method == "POST":
    data = request.get_json()
    diseases = data[0] #array of selected diseases from HTMl dropdown
    drugs = data[1]  #array of selected drugs

    def output_array(array, path): #if you want to write, then read back in later
      with open(path, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(array)

    #output_array(diseases, 'text.txt')


    driver.driver(drugs)

    #insert computational code here
    #output results to a json file please
    #i've provided an edited put_data function


    print(diseases)
    print(drugs)

  results = {'processed': 'true'}
  return jsonify(results)

if __name__ == "__main__":
  app.run(debug=True)
