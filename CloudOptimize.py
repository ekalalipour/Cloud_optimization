#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis

"""

import os
import random
import subprocess

def is_running_on_cluster():
    if 'SLURM_ARRAY_TASK_ID' in os.environ:
        return int(os.environ['SLURM_ARRAY_TASK_ID'])
    return int(-1)

def create_cog(src, dst, block_size=512, compress='RAW'):
    ''' 
    creating cloud optimize geotiff
    '''
    #creating a dictionary that contains (key values) options
    out_profile = {
        'tiled': 'YES',
        'blockxsize': block_size,
        'blockysize': block_size,
        'compress': compress,
    }    
    # creating a command for subprocess to pass it to osgeo
    # making a list from items in out-profile
    options = [''.join(['-co ', key.upper(), '=', str(out_profile[key])]) for key in out_profile]
    # concatenating all the items with a space
    # * unpacks the list so the .join can concatenate the options
    translate_command = ' '.join(['gdal_translate -of GTiff', *options, src, dst])
    #print(*options)
    print(translate_command)
    subprocess.run(translate_command, shell=True)

def scan_directory(d):
    '''
    Scans the directory and looks for file that ends 
    with .tif and put them in tiff-files list
    '''
    
    print(d)
    tiff_files = []
    # os.walk generate file names in directory tree by walking the tree
    for (dirpath, dirs, files) in os.walk(d):
        for file in files:
            if file.endswith('.tif'):
                tiff_files.append(os.path.join(dirpath, file))
    #print(tiff_files)
    return tiff_files

def read_catalog(src):
    with open(os.path.join(src, 'catalog.txt')) as catalog:
        tiff_files = catalog.readlines()
    return tiff_files

def create_catalog(src):
    '''
    Catalog tiff files to a text file
    '''
    tiff_files = scan_directory(src)
    print(len(tiff_files)) # Print the number of files
    path = os.path.join(src, 'catalog.txt')
    txt_file = open(path, 'w')
    for tiff_file in tiff_files:
        txt_file.write(tiff_file + '\n')
    txt_file.close()
    return path

def convert_tiff_file(tiff_file, src, dst):
    '''
    creates a catalog of tiff files. also, makes parallel path, and if the output path doesnt exist it creats one
    '''
    folder, base = os.path.split(tiff_file)
    folder = folder.replace(src, dst)
    if not os.path.exists(folder):
        os.makedirs(folder)
    out = os.path.join(folder, base)
    print('converting', tiff_file, 'to', out)
    create_cog(tiff_file.strip(), out.strip(), compress='LZW', block_size = 512)

def random_select(src):
    '''
    TODO: What does this function do? Randomly select tif files for COG validation
    '''
    tiff_files = read_catalog(src)
    n = len(tiff_files)
    percent = 0.1
    r = random.sample(list(range(n)), max(int(percent * n), 1))
    
    #TODO: What is this loop for?
    #for i in r:
    #    convert_tiff_file(tiff_files[i], src, dst)
    
    return [tiff_files[i] for i in r]

def main(src = "C:\\Users\\Emad\\Desktop\\test", dst = "C:\\Users\\Emad\\Desktop\\cog"):
    '''
    the main is for testing
    '''
    tiff_files = scan_directory(src)
    for tiff_file in tiff_files:
        convert_tiff_file(tiff_file, src, dst)
    create_catalog(dst)

if __name__=="__main__":
    main()