#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 07:18:44 2020

@author: mark
"""

# Store input filename in variable. Include necessary path info.
in_filename = "data/apache-mini.log"

# Init counter to keep track of line numbers (not necessary but sometimes useful)
line_number = 0

# Create empty list
loglines = []

# Open the input file for reading
with open(in_filename, 'r') as in_file:
    # Loop through each line in the file. Check out the nice looping syntax for traversing a file.
    for line in in_file:
        
        # Let's strip off any end of line characters
        line = line.rstrip()
        
        # Before we split on the spaces, let's get rid of the brackets around the date
        line = line.replace('[', '')
        line = line.replace(']', '')
        
        # Now split the line using space as our delimiter
        logline_list = line.split(' ')
        
        # Append the logline list to the master list
        loglines.append(logline_list)
        
        # Increment the line counter
        line_number += 1
        
# All done, print the list
print(loglines)