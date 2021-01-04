import requests
import shutil

def getImage(image_url, filename, urlPrefix='', fileExtension='.jpg'):

    r = requests.get(urlPrefix + image_url + fileExtension, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print("Succesfully downloaded image")

    else:
        print("Error getting image")