"""
Read files
File position:
* read()        : Returns the entire file
* seek(offset)  : Change the current position to offset
* seek(0)       : Go to the beginning of the file
* seek(5)       : Go to the 5th byte of the file
* tell()        : Determine the current position in the file
"""
"""
open(path_to_file, mode)
Mode    Description
--------------------
r       Open for reading(default)
w       open for writing, truncating first
x       Create a new file and open it for writing
a       Open for writing, appending file
+       Open a file for updating (read / write)
b       Binary mode
t       Text mode (default)
"""

# hosts = open('C:/Windows/System32/drivers/etc/hosts')
# hosts_file_content = hosts.read()
# print(hosts_file_content)
# hosts.close()

# Automatic close the file (better approach)
# ------------------------------------------
# print("\n\n")
# with open('C:/Windows/System32/drivers/etc/hosts') as f:
# 	print('File closed ? {}'.format(f.closed))
# 	print(f.read())
# print('Finished reading the file.')
# print('File closed ? {}'.format(f.closed))

# read file line by line
with open('C:/Windows/System32/drivers/etc/hosts') as f:
	for line in f:
		print(line.rstrip())

