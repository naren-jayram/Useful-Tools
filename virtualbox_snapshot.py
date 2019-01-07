'''
Objective: This script is used to automate the virtualbox snapshots with VBoxManage command
Pre-requisite: 1. VirtualBox has to installed
               2. Set the environment variables. Path =  'C:\Program Files\Oracle\VirtualBox'
Usage: python virtualbox_snapshot.py
'''

#!/usr/bin/python
import datetime
import time
import os

now = datetime.datetime.now()
snapshotName ="snap1" 											# Choose the name of the snapshot
vm_name = "Ubuntu 12.04 LTS 32 Bits"                            # Input your VM name
snapshotDescription = "Snapshot taken on %s" %now


snapshot= os.system('VBoxManage snapshot "%s" take "%s" --description "%s"' %(vm_name,snapshotName,snapshotDescription))


#Now, add the below entry to your cron to run once every day at 12 AM; Note: This is as per your requirements.
#  0 0 * * * /place where this script resides/VirtualboxSnapshot.py 