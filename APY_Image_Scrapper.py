from api_image_getter import getImage
from api_request import makeRequest
from json_parser import parseJSONFile
import argparse, sys
import os.path as path
from pathlib import Path
import time

parser = argparse.ArgumentParser()
parser.add_argument('--path', '-p', type=str, help='the path where the images will be saved')
parser.add_argument('json', metavar='json', type=str, help='the path to a json file containing the information for the api call')

args = parser.parse_args()

data = parseJSONFile(args.json)

response = makeRequest(data)

if path.isabs(args.path): 
    destPath = args.path
else:
    destPath = path.join(Path().absolute(), args.path)

imageCounter = 0

for item in response:
    auxFilename = item[data['keyToUse']]
    auxPath = path.join(destPath, auxFilename) + data['fileExtension']

    getImage(auxFilename, auxPath, data['urlPrefix'], data['fileExtension'])

    imageCounter += 1

    if(imageCounter % 10 == 0):
        print(f"Saved {imageCounter} of {len(response)} images")
        time.sleep(10)