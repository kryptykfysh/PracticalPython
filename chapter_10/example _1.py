#!/usr/bin/env python3

# Write a program that makes a backup of a file. Your program should
# prompt the user for the name of the file to copy and then write a new file
# with the same contents but with .bak as the file extension.

file_to_backup = input('Enter a file name: ').strip()

with open(file_to_backup) as file:
    data = file.read()

new_file_name = file_to_backup[:(file_to_backup.index('.')) + 1] + 'bak'

with open(new_file_name, 'w') as file:
    file.write(data)
