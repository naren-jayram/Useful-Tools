# Objective: To identify whether a given URL is static or Dynamic (when you are examining bulk URLs)


# Usage:
# 1. Create a file, <input.txt> and place all the urls in it. Please make sure  each URL goes in a new line.
# 2. python static_page_detection.py
# 3. Result will reside in output.csv


# Note: 1. This is just a starting point. Please don't completely rely on this strategy. 
#       2. This is written in python v2.7

#! /usr/bin/python
import re
import csv

#Config
matches = 0
static_message = 'Seems to be a static web page'
dynamic_message = 'Seems to be a dynamic web page'
static_extensions = '\.png$|\.jpg$|\.jpeg$|\.gif$|\.css$|\.ico$|\.js$|\.woff$|\.bmp$|\.pict$' #You can add more static extensions here
#End of Config


def write_csv(url, status):
    with open ('output.csv', 'a') as csvfile:
      write_descriptor = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL )
      write_descriptor.writerow([url, status])


# Writes header info to output.csv
with open('output.csv', 'w+') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header_list = ['URL', 'Result']
    csvwriter.writerow(header_list)


with open('input.txt', 'r') as url:
    urls = url.readlines()

for url in urls:
    clean_url = url.replace(' ', '').replace('\n', '')
    matches = re.findall(static_extensions, clean_url)
    if len(matches) == 0: 
   	    write_csv(url, dynamic_message)
    else:
   	    write_csv(url, static_message)