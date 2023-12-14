import csv
import json

def csv_to_json(csvFilePath,jsonFilePath):
    with open(csvFilePath,'r')as csvf:
        csvReader = csv.DictReader(csvf)

        dict = {}
        index = 0
        for row in csvReader:
            key = index
            dict[key] = row
            index += 1
    with open(jsonFilePath,'w')as jsonf:
        jsonf.write(json.dumps(dict,indent=4))

csvFilePath = r'products.csv'
jsonFilePath = r'elokoniec.json'

csv_to_json(csvFilePath, jsonFilePath)
