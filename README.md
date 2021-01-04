# APY_Image_Scrapper
An image scrapper made in python to get all the images from the response of an api request. It makes an api request and then proceeds to get download all the images from the response object. 

## The CLI
The CLI has two parameters, one required and one optional. 

**Required**

The required arguement is a positional arguement that taks the path to a json file containing the arguements for the scrapper.

**Optional**

The optional arguement is the path to the directory where the images will be saved, if none is given it will save the images in the directory where the script is located.

## The Arguements JSON
The arguements json can have the next values:

**Required**
  - url: Contains the url endpoint for the api request
  - keyToUse: Contains the name of the key that will be accessed in the response object

**Optional**
  - headers: Contains an json object with the necessary headers to make the api request
  - urlPrefix: A prefix that can be added to the keyToUse
  - fileExtension: The file extension of the images to get, the deafult value is ".jpg"
