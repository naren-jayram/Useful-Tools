"""
Objective: Bulk forward DNS ('A' Record) lookup 

Usage: 
		1. Create a file, <input.txt> and place all the host names in it. Please make sure each host name goes in a new line.
		2. python bulk_nslookup.py
		3. Output resides in <output.csv>

Note: Written in Python v2.7
 """

#!/usr/bin/python
import commands
import csv
import re

# Variables
clean_hostnames = []
nslookup_result = []
# End of Variables

with open('input.txt','r') as hostname:
    host_names = hostname.readlines()

for host in host_names:
	clean_host = host.replace(' ', '').replace('\n', '')
	clean_hostnames.append(clean_host)



with open('IP_Details.log', 'w+') as file:
	for host in clean_hostnames:
		print (host)
		log_cmd= "nslookup %s 2>&1" %host
		output = commands.getoutput(log_cmd)
		
		file.write("**********************************************************\n")
		file.write("%s\n" %host)
		file.write("%s\n" %output)
		try:
			#regex = re.search("Name:.*Address:[\s]+([\d\.]+).*", output)
			regex = re.search("Name:[\s\\t]+[\w\-.]+\\nAddress:\s+([\d\.]+)", output)
			ip_address = regex.groups()[0]
			nslookup_result.append([host, ip_address])
		except Exception as e:
			print (e)
			continue


# Writing output to CSV file
with open('output.csv', 'w+') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header_list = ['Name', 'Address']
    csvwriter.writerow(header_list)
    for result in nslookup_result:
    	csvwriter.writerow(result)

