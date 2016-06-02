#!/usr/bin/env python

import os
import re
import glob
from collections import Counter
from sets import Set

content = Counter()

files = glob.glob("nasdaqth*")
ordered_files = sorted(files, reverse=True)
previous = None

for file in ordered_files:
    print file
    m = re.match(r'nasdaqth(.*)\.txt', file)
    with open(file) as f:
        current = Set()
        for line in f.readlines():
            fields = line.split('|')
            if fields[0] != 'Symbol' and not re.match(r'^2016', fields[0]):
                current.add(fields[0])

        if previous is None:
            previous = current
            content.update(current)
        else:
            intersect = current.intersection(previous)
            print intersect
            content.update(intersect)





print content
