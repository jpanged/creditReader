# Project: Google Cloud Credit Code Reader
# Author: Josiah Pang
# Spring 2018
# This program takes images of GCP Credits and outputs their individual unique
# codes. It was written to help Student Innovators track credit activations.

# Import libraries
import config
import io
import os
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def main():
    detect_text_uri('gs://' + config.CLOUD_STORAGE_BUCKET + '/credits-04.jpg')

# For label detection
def detect(labels):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'images/credits-02.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)

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
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

if __name__ == '__main__':
    main()
