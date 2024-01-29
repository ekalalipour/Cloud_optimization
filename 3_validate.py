#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis
"""

import os
import sys
import CloudOptimize
import validate_cloud_optimized_geotiff

if __name__=="__main__": 
    #Get the input directory from arguments
    if len(sys.argv) >= 2:
        src = sys.argv[1]
    else:
        print("Requires argument for source directory to validate")
        exit()

    # Read the catalog
    #CloudOptimize.create_catalog(src) # this makes a catalog, we want to read an existing catalog and make one if missing

    # Random sample 10 % of files
    tiff_files = CloudOptimize.random_select(src)

    # Validate those files as cog
    path = os.path.join(src, 'validation.txt')
    
    validations = [validate_cloud_optimized_geotiff.validate(tiff_file.strip()) for tiff_file in tiff_files]
    print(validations)
    txt_file = open(path, 'w')
    # Write results of validation to file
    for validation in validations:
        txt_file.write(str(validation) + '\n')
    txt_file.close()
    # Report on success/error rate
