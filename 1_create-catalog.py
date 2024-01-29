#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis

"""

import sys

# Custom Functions
import CloudOptimize

if __name__=="__main__": 
    if len(sys.argv) >= 2:
        src = sys.argv[1]
        
        x = CloudOptimize.create_catalog(src)
        
        #TODO: print the name/location of the catalog file, and number of items included
        print("name:" ,x)
    else:
        print("Requires argument for source and destination directory")
        exit()
