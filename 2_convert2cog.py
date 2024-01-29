#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis

"""

import sys
import os
import CloudOptimize


def convert_catalog(src, dst):
    '''
    TODO: Document arguments to function
    '''
    catalog = os.path.join(src, 'catalog.txt')
    try:
        fp = open(catalog, 'r')
    except IOError:
        print("catalog does not exist")
        exit()
    # If on cluster get ARRAY TASK ID
    line = CloudOptimize.is_running_on_cluster()
    if line >= 0:
        for i, tiff_file in enumerate(fp): #enumerate allows us to have a automatic counter for iteration
            if i == line:
                print("converting:", tiff_file)
                CloudOptimize.convert_tiff_file(tiff_file, src, dst)
                #break
    else:
        # If local list of files to convert
        for i, tiff_file in enumerate(fp):
            print("converting:", tiff_file)
            CloudOptimize.convert_tiff_file(tiff_file, src, dst)
    fp.close()
    return True

if __name__=="__main__": 
    #Get the input and output directories from arguments
    if len(sys.argv) >= 3:
        src = sys.argv[1]
        dst = sys.argv[2]
 
        check = convert_catalog(src, dst)
            
    else:
        print("Requires argument for source and destination directory")
        exit()