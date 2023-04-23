#!/usr/bin/env python3
# Author: Your Name; youremail@myseneca.ca
# Date:
# Purpose: Backs up virtual Machines
# Usage: ./backupVM.py
#

# Import the Operating System (os) module, Subprocess module and Sys module


# Store the output of the whoami command as a variable called whoami


# Check the current user (who is executing the script) and store the information in the variable currentuser.  The os.geteuid() command requests the current user ID from the operating system.  Root has a UID of (0).  Users have non-zero values, usually starting at 1000.  We can use this to check if the current user is root or not.


# Using an if statement check if currentuser is not equal to 0


	# Print a message telling the user who they are.  Use , to concatenate (join) the message and the whoami variable
	

	# Exit with an error message indicating they must be root
	

# Else (they are root, we can continue)


	# Prompt the user asking if they wish to back all VMs, accepting options y for yes or n for no.  Store the answer in the variable backupAll
	

	# If backupAll equals "n"
	
		
		# Prompt the user asking which VM they wish to backup.  Store the answer in the variable backupVM
		
		
		# If backupVM equals "centos1"
		

			# Print "Backing up centos1"
			

			# Use os.system to call the virsh dumpxml command you used for centos1 in Lab 2 Investigation 3
			

			# Use os.system to compress (using gzip) the .qcow2 for centos1, using the same syntax as in Lab 2 Investigation 3
			

		# Else if (elif) backupVM equals "centos2"
		

			# Print "Backing up centos2"
			

			# Use os.system to call the virsh dumpxml command you used for centos2 in Lab 2 Investigation 3
			

			# Use os.system to compress (using gzip) the .qcow2 for centos2, using the same syntax as in Lab 2 Investigation 3
			

		# Else if (elif) backupVM equals "centos3"
		

			# Print "Backing up centos2"
			

			# Use os.system to call the virsh dumpxml command you used for centos3 in Lab 2 Investigation 3
			

			# Use os.system to compress (using gzip) the .qcow2 for centos3, using the same syntax as in Lab 2 Investigation 3
			

		# Else, user has entered an invalid choice
		
			
			# Display a message indicating an invalid choice has been made and give the valid options (centos1, centos2, centos3) and exit
			

	# Else, we're doing a full backup (backing up all 3 virtual machines: centos1, centos2, centos3)
	

		# Print "Backing up centos1"
		

		# Use os.system to call the virsh dumpxml command you used for centos1 in Lab 2 Investigation 3
		

		# Use os.system to compress (using gzip) the .qcow2 for centos1, using the same syntax as in Lab 2 Investigation 3
		

		# Print "Backing up centos2"
		

		# Use os.system to call the virsh dumpxml command you used for centos2 in Lab 2 Investigation 3
		

		# Use os.system to compress (using gzip) the .qcow2 for centos2, using the same syntax as in Lab 2 Investigation 3
		
			
		# Print "Backing up centos3"
		

		# Use os.system to call the virsh dumpxml command you used for centos3 in Lab 2 Investigation 3
		

		# Use os.system to compress (using gzip) the .qcow2 for centos2, using the same syntax as in Lab 2 Investigation 3
		

		# Exit successfully
		
