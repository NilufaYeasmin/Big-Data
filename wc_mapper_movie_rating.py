#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split("\t")
    if words[0] == 'A':
        if int(words[3]) > 3:
            print '%s\t%s' % (words[2], str(words[0]) + "_"  + str(words[3]))
    else:
        print '%s\t%s' % (words[1], str(words[0]) + "_" + str(words[2]))
    #print words

