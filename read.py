# Project: Google Cloud Credit Code Reader
# Author: Josiah Pang
# Spring 2018
# This program takes images of GCP Credits and outputs their individual unique
# codes. It was written to help Student Innovators track credit activations.
# It can either take local images or images hosted on a Google Cloud Storage
# Bucket. The program returns an 'out.txt' file with the codes separated by a
# new line in addition to printing to the console. Store local images in the
# "/images" folder.

# Import libraries
import config
import io
import os
import re
from sys import *

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def main(): # Uncomment the function you want to use (local vs cloud storage)
    try:
        # For local images
        img_path = os.path.join(path[0], 'images/' + argv[1])
        detect_text(img_path)

        # For images hosted on Cloud Storage Bucket
        #detect_text_uri('gs://' + config.CLOUD_STORAGE_BUCKET + '/' + argv[1])
    except:
        print("Usage: python read.py IMAGE_NAME")


# For remote images
def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Prep file for writing
    outFile = open('out.txt', 'w+')

    # Traverse detected text and only save valid codes
    prev = ''
    pattern = '[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]'
    for text in texts:
        cur = '{}'.format(text.description)
        if re.match(pattern, cur): # Use regex to identify code
            print(cur)
            outFile.write(cur + '\n')
        prev = cur

    # Close written file
    outFile.close()


# For local images
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Prep file for writing
    outFile = open('out.txt', 'w+')

    # Traverse detected text and only save valid codes
    prev = ''
    pattern = '[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]-[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]'
    for text in texts:
        cur = '{}'.format(text.description)
        if re.match(pattern, cur): # Use regex to identify code
            print(cur)
            outFile.write(cur + '\n')
        prev = cur

    # Close written file
    outFile.close()

if __name__ == '__main__':
    main()