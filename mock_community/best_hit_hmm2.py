#!/usr/bin/python
# usage: python best_hit_hmm.py imput > output
import sys
d = {}
for line in open(sys.argv[1],'r'):
    if (line[:1] == "#"):
        continue
    spl = line.strip().split(' ')
    sto = []
    for x in spl:
        if not (x == ""):
            sto.append(x)
    query = sto[2].strip()
    hit = spl[0].strip()
    if d.has_key(query):
        continue
    else:
        d[query] = hit
        print line,
