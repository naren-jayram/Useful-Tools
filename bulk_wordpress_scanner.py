"""
OBJECTIVE: Bulk wordpress scanner 

PRE-REQUISITE: Install wpscan from https://github.com/wpscanteam/wpscan

USECASES: 1. You have been given a list of URLs to find if they are powered by wordpress 
		  2. Scanning many wordpress powered URLs/ websites at once

Why I wrote this tiny script?
https://github.com/wpscanteam/wpscan takes one URL at a time. This limitation will be overrided with this script.

USAGE: 	1. Create a file, <input.txt> and place all the URLs in it. Please make sure each URL goes in a new line.
		2. python bulk_wordpress_scanner.py 
		3. Scanning results will be exported to <output.csv> file

Credits: WPScan Team

Root Project: https://github.com/wpscanteam/wpscan

Note: You can play with different wpscan arguments 
"""

#!/usr/bin/python
import commands
import csv

#Variables
wp_command = "wpscan -e -r --follow-redirection --batch --disable-tls-checks --no-banner" 	# wpscan command
clean_url_list = []
# End of variables

with open('input.txt', 'r') as url:
	url_list = url.readlines()

for url in url_list:
	clean_url = url.replace(' ', '').replace('\n', '')
	clean_url_list.append(clean_url)


# Writing output to CSV file
with open('output.csv', 'w+') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header_list = ['URL', 'Result']
    csv_writer.writerow(header_list)
    for url in clean_url_list:
    	print url
     	cmd = wp_command + " -u %s 2>&1" %url
		output = commands.getoutput(cmd)
		csv_writer.writerow([url,output])

