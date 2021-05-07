#!/usr/bin/python3
from Node import *

import sys
import re

#new input patter for the data
input_pattern = re.compile(r"""
    (\w+)
    \s+
    (\d+) """, re.VERBOSE)
input_filename= "france-roads1.txt"   #the input file name

input_records = 0
outer_dict = {}
input_file= open(input_filename)
bof_flag = True
prev_record = 'xxx'
inner_dict = {}
outer_key = ''
node_list = []

#for each input record in the input file
#read in the input record into a dict of dict 
#the dict of dict represents the france maps
for input_record in input_file:
    input_records += 1

    if bof_flag:
        outer_key = input_record.strip()
        outer_key = outer_key.replace(":","")
        bof_flag = False

    elif(input_record == '\n'):
        outer_dict[outer_key] = inner_dict
        bof_flag = False

    elif(prev_record == "\n"):
        inner_dict = {}
        outer_key = input_record.strip()
        outer_key = outer_key.replace(":","")
        outer_key = outer_key.capitalize()

    else:
        m = input_pattern.match(input_record)
        if not m:
            exit(1)
        m_distance_type = m.group(1)
        m_distance = m.group(2)
        inner_dict[m_distance_type] = m_distance

    prev_record = input_record


input_file.close()

