#!/bin/env python

import sys

#dictionary to store each word as key and their total count as value
word_dict = {}


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    words, count =line.split('\t', 1)
    #words, count = line.split(' ')   #when fields are separated by space as in animal_100.txt

    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if words not in word_dict:
        word_dict[words] = count
    else:
        word_dict[words] = word_dict[words]+ 1

#sort dictionary value on descending order of the total count
word_dict_sort = [(k,word_dict[k]) for k in sorted(word_dict,key=word_dict.get,reverse=True)]

#Get the maximum occurred n words from the sorted dictionary when n=10

step=0
n=10
for k,v in word_dict_sort:
    if step < n:
        print k,v
        step+=1
    else:
        break