"""
Objective: Bulk Reverse DNS ('PTR' Record) Lookup 

Usage: 
		1. Create a file, <input.txt> and place all the IP addresses in it. Please make sure each IP Address goes in a new line.
		2. python bulk_reverse_lookup.py
		3. Output resides in <output.csv>

Note: 
1. Written in Python v2.7
2. DIG Utility should be installed
"""

#!/usr/bin/python
import commands
import csv
import re

# Variables
clean_hostnames = []
lookup_result = []
# End of Variables

with open('input.txt','r') as hostname:
    host_names = hostname.readlines()

for host in host_names:
	clean_host = host.replace(' ', '').replace('\n', '')
	clean_hostnames.append(clean_host)



for host in clean_hostnames:
	print (host)
	try:
		log_cmd= "dig -x %s +short 2>&1" %host
		output = commands.getoutput(log_cmd)
		lookup_result.append([host, output])
	except Exception as e:
		print (e)
		continue


# Writing output to CSV file
with open('output.csv', 'w+') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header_list = ['Address', 'Name']
    csvwriter.writerow(header_list)
    for result in lookup_result:
    	csvwriter.writerow(result)


# In Shell Scripting its a single liner
#cat input.txt |   while read -r line ; do echo "$line" | dig -x $line +short;   done;