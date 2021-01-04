import json

def parseJSONFile(filename):
    
    with open(filename) as f:
        data = json.load(f)

    return data