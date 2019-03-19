#!/usr/bin/env python

import jemdoc
import os

cmd = "python jemdoc.py -c .\\mysite.conf .\\jem\\"

for r, d, f in os.walk(".\\jem"):  
    for fn in f:
        os.system(cmd + fn)

print("Hello sailor!")
