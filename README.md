# Google Cloud Platform Credit Reader

## Overview:
This is a tool I created to help Student Innovators keep track of their GCP
credit activations. SIs can take pictures of their credit vouchers and run
them through this program to get a text output to which helps them digitally
track redemptions. Having digital strings of the codes have many helpful
applications such as being used for event raffles or distributing to students
digitally.

creditReader uses the Google Cloud Vision API's OCR technology to extract all
the text from images of credit vouchers. I then use regular expressions to find
codes according to their predictable pattern. Each code is then saved to a new
line of a text file and printed to the console terminal.

## Requirements:
* [Python 3.x](https://www.python.org/downloads/)
* google-cloud Python library
```
pip install --upgrade google-cloud
```

## Usage:
```
python read.py IMAGE NAME OUTPUT.txt
```
Example: `python read.py ex1.jpg out1.txt`

*Note: Put images in /images/ folder*
