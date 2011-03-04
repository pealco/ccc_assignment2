#!/usr/bin/env python
# encoding: utf-8
"""
translation.py

Created by Pedro Alcocer on 2011-03-01.

Using combiners.
"""
import dumbo
from collections import defaultdict

def mapper(key, value):
    for trans in value.split():
        english, french = trans.split("::")
        yield english, (french, 1)

def reducer(key, values):
    sum = 0.0
    counts = defaultdict(int)
        
    for word, count in values:
        counts[word] += count
        sum += count
    
    for word in counts:
        yield (key, word), counts[word]/sum

def combiner(key, values):
    counts = defaultdict(int)
    
    for word, count in values:
        counts[word] += 1
    
    for word in counts:
        yield key, (word, counts[word])

if __name__ == '__main__':
    dumbo.run(mapper, reducer, combiner=combiner)

