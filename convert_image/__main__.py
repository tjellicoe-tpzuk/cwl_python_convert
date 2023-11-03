## A duplicate of the convert.sh file, but this time written in Python.
#  Depending on success here, this will inform potential to include OpenEO commands within the EOEPCA application package

from PIL import Image
import math
import sys
import requests
from io import BytesIO
import PIL.ImageOps
import os
import json

## function to determine function to be done, here only resize or invert
def do_func(args): # input is --fn invert --url "url" --size "ss"
    func = args[1]
    print(func)
    if func == "resize":
        ##call resize func
        convert_get_type(args)
    elif func == "invert":
        ##call invert func
        invert_get_type(args)
    else:
        raise Exception('This function is not supported in current implementation', func)


## function to determine whether url or stac object to be converted
def convert_get_type(args):
    srcType = args[2]
    size = args[4]
    if srcType == "--url":
        input_file = args[3]
        convert_url(input_file, size)
    elif srcType == "--stac":
        input_dir = args[3]
        convert_stac(input_dir, size)
    elif srcType == "--file":
        input_file = args[3]
        convert_file(input_file, size)
    else:
        raise Exception()


## function to determine whether url or stac object to be inverted
def invert_get_type(args):
    srcType = args[2]
    if srcType == "--url":
        #invert_url(args)
        None
    elif srcType == "--stac":
        #invert_stac(args)
        None
    elif srcType == "--file":
        #invert_file(args)
        None
    else:
        raise Exception()

def convert_url(url_name:str, size:str):
    domainName = os.path.dirname(url_name)
    outName = url_name.replace(domainName + "/", "")
    outName = outName.replace(".", f"scaled_by_{size}-NEW.")
    #fileType = os.path.splitext(url_name)

    response = requests.get(url_name)
    with Image.open(BytesIO(response.content)) as im:
        out_size = percent_to_num(size)
        out_size_tuple = size_to_tuple_url(url_name, out_size)
        out_im = im.resize(out_size_tuple)
        out_im.save(outName)

def convert_stac(file_dir:str, size:str):

    ## open file directory
    catFileLocation = open(file_dir + "/catalog.json")
    ## open catalog.json
    #print(fileLocation)
    jsonFile = json.load(catFileLocation)
    
    ## identify href of links, .rel object
    fileName = -1
    for i in range(len(jsonFile['links'])):
        print(jsonFile['links'][i])
        if jsonFile['links'][i]['rel'] == "item":
            fileName = [jsonFile['links'][i]['href']]
            break
    ## take file name obtained from above .rel link
    print(fileName)
    if fileName == -1:
        raise Exception("Required JSON file not found in directory", file_dir)
    
    ## identify, via href, the final png to be editted
    jsonFileLocation = open(file_dir + "/" + fileName[0])
    jsonFile = json.load(jsonFileLocation)
    fileName = jsonFile['assets']['logo']['href']
    print(fileName)

    outName = fileName.replace(".", f"scaled_by_{size}-NEW.")
    imgFileLocation = file_dir + "/" + fileName
    ## convert file as before, then update STAC data in JSON (new function for this)

    with Image.open(imgFileLocation) as im:
        out_size = percent_to_num(size)
        out_size_tuple = size_to_tuple_file(imgFileLocation, out_size)
        out_im = im.resize(out_size_tuple)
        print("here " + outName)
        out_im.save(outName)

def convert_file(file_name:str, size:str):
    print("HERE")
    dirName = os.path.dirname(file_name)
    outName = file_name.replace(dirName + "/", "")
    outName = outName.replace(".", f"_scaled_by_{size}-NEW.")
    with Image.open(file_name) as im:
        #im.show("Orignal Image")
        out_size = percent_to_num(size)
        out_size_tuple = size_to_tuple_file(file_name, out_size)
        out_im = im.resize(out_size_tuple)
        print("here " + outName)
        #outName = "outimage.png"
        out_im.save(outName)

def invert_file(file_name:str, size:str):

    with Image.open(file_name) as im:
        #im.show("Orignal Image")
        out_im = PIL.ImageOps.invert(im)
    return out_im

## Convert input size string to a double - removing percentage

def percent_to_num(percentage:str):
    
    if percentage.find("%") == -1:
        raise Exception("Size input is not a percentage, please ensure input ends in '%'")
    else:
        percentage = percentage.replace("%","")
        return float(percentage)


def size_to_tuple_file(file_name:str, size:float):
    image = Image.open(file_name)
    curr_size = image.size
    #print(curr_size)

    #new_size = []
    scale_factor = size/100 ## note, this reduces image size both in the width and height directions

    new_size = [int(math.ceil(x*scale_factor)) for x in curr_size]
    #print(new_size)

    return new_size

def size_to_tuple_url(url_name:str, size:float):
    response = requests.get(url_name)
    image = Image.open(BytesIO(response.content))
    curr_size = image.size
    #print(curr_size)

    #new_size = []
    scale_factor = size/100 ## note, this reduces image size both in the width and height directions

    new_size = [int(math.ceil(x*scale_factor)) for x in curr_size]
    print(new_size)

    return new_size


def create_output_stac():
    create_stac_item()
    create_stac_catelog_route()

def create_stac_item():
    None

def create_stac_catelog_route():
    None

def convert_main(args: [str]):
    if len(args) == 1:
        raise Exception("no arguments provided, please provide file_name and increase_size")
    file_name = args[1]
    file_name_no_ext = args[1].replace(".png", "")
    increase_size = args[2]
    do_func(args)#.save(f"{file_name_no_ext} resized to {increase_size}.png")

if __name__ == "__main__":
    convert_main(sys.argv)




#convert_image("logo6_med.original-resize.png", "10%")
# increase_size = "200%"

# response = requests.get("https://eoepca.org/media_portal/images/logo6_med.original.png")
# img = Image.open(BytesIO(response.content)).save("test image.png")


# convert_image("https://eoepca.org/media_portal/images/logo6_med.original.png", increase_size).save(f"resized image {increase_size}.png")

