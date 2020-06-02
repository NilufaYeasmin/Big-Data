#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
tableA = []
tableB = []
key = None
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    try:
        words = line.split('\t')
        key = words[0]
        second = words[1]
        table = second.split("_")[0]
        value = second.split("_")[1]
    except:
        continue

    if current_key == key:
        if table == 'A':
            rating = value
            tableA.append(value)
        if table == 'B':
            tableB.append(value)
    else:
        if current_key:
            if tableA:
                if tableB:
                    for rating in tableA:
                        for movie_name in tableB:
                            print '%s\t%s' % (movie_name, rating)
        current_key = key
        tableA = []
        tableB = []
        if table == 'A':
            tableA.append(value)
        if table == 'B':
            tableB.append(value)

if current_key == key:
    if tableA:
        if tableB:
            for rating in tableA:
                for movie_name in tableB:
                    print '%s\t%s' % (movie_name, rating)