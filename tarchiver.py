#!/usr/bin/env python3
# Author: Your Name, youremail@myseneca.ca
# Date:
# Purpose: Creates a tar archive of a directory, with optional compression
# Usage ./tarchiver.py
#

# Import the Operating System and sys modules


# 2: Ask the user what directory they wish to archive, store the output in the variable backupSource


# 2: Ask the user what they want the archive to be called


# 3: Create an archive using the above choices, using the tar command


# Debugging statements to confirm variables are working properly, uncomment these to test, comment them out when done.  Remove in production code.
#print("backupName: ",backupName)
#print("backupSource: ",backupSource)

# Use the join operator to combine our variables with the tar command syntax.  Store this in the variable cmd.


# Debugging statement to confirm cmd is being created properly
#print(cmd)

# Call the command using os.system


# 5: Ask the user if they wish to compress the archive, accept answers y or n


# 7: If compression equals y, compress the archive


	# Ask the user what type of compression they would like to use


	# If compressionType equals gzip, zip the archive with gzip

	
		# Create a variable called compress and store the command in it


		# Call gzip with backupName.tar as the argument using os.system


	# else if compressionType equals bzip2


		# Create a variable called compress and store the command in it

		
		# Call bzip2 with backupName.tar as an argument using os.system


	# else if compressionType equals xzip


		# Create a variable called compress and store the command in it


		# Call xzip (xz) with backupName.tar as an arguement using os.system


	# Else, throw an error and exit


		# Use sys.exit to exit with a meaningful error message


# Else, we are done


	# exit successfully using sys.exit (with a zero exit code)

