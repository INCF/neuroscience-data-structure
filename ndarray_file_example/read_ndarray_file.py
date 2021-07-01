#!/usr/bin/env python3

import numpy as np
import json

folder = './'
filename = folder + 'FileSpec2.3001.ns5'


with open('header.json', 'r') as f:
    d = json.load(f)

sigs = np.memmap(filename, mode='r',
    dtype=d['dtype'],
    offset=d['offset'],
    shape=tuple(d['shape']),
    order='C')

print(sigs.shape, sigs.dtype) 
