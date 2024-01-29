# Cloud Optimization

Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis

The goal of these scripts is to batch convert geotiffs to cloud optimized geotiffs (COGS).

This code scans the directory and looks for tiff file and creates a catalog of tiff files into a txt file in the directory, so the user can run the cog on either the whole file or a specific file in the catalog.

source code:https://github.com/sshuair/cogeotiff/blob/master/cogeotiff/cog.py
            https://github.com/sshuair/cogeotiff/blob/master/cogeotiff/cog.py

Osgeo command line > C:\\Users\\Emad\\Desktop\\CloudOptimize.py C:\Users\Emad\Desktop\test
 
To generate COG in command line > >gdal_translate C:\\Users\\Emad\\Documents\\sUAS\\AEBB_20180813_X3.tif C:\\Users\\Emad\\Documents\\sUAS\\input\\AEBB_20180813_X3_cog.tif -co TILED=YES -co / COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW

To validate the COG in command line >> python3 C:\\Users\\Emad\\Documents\\sUAS\\validate_cloud_optimized_geotiff.py C:\\Users\\Emad\\Documents\\sUAS\\test.tif

example of code in command line:

C:\>python3 "C:\Users\Emad\Desktop\2ndscript.py" C:\Users\Emad\Desktop\test

['C:\\Users\\Emad\\Desktop\\test\\AEBB_20180813_X3_com.tif', 'C:\\Users\\Emad\\Desktop\\test\\1\\AEBB_20180813_X3_com.tif', 'C:\\Users\\Emad\\Desktop\\test\\1\\2\\AEBB_20180813_X3_com.tif']
converting C:\Users\Emad\Desktop\test\AEBB_20180813_X3_com.tif to C:\Users\Emad\Desktop\cog\AEBB_20180813_X3_com.tif
gdal_translate -of GTiff -co TILED=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co COMPRESS=LZW C:\Users\Emad\Desktop\test\AEBB_20180813_X3_com.tif C:\Users\Emad\Desktop\cog\AEBB_20180813_X3_com.tif
converting C:\Users\Emad\Desktop\test\1\AEBB_20180813_X3_com.tif to C:\Users\Emad\Desktop\cog\1\AEBB_20180813_X3_com.tif
gdal_translate -of GTiff -co TILED=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co COMPRESS=LZW C:\Users\Emad\Desktop\test\1\AEBB_20180813_X3_com.tif C:\Users\Emad\Desktop\cog\1\AEBB_20180813_X3_com.tif
converting C:\Users\Emad\Desktop\test\1\2\AEBB_20180813_X3_com.tif to C:\Users\Emad\Desktop\cog\1\2\AEBB_20180813_X3_com.tif
gdal_translate -of GTiff -co TILED=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co COMPRESS=LZW C:\Users\Emad\Desktop\test\1\2\AEBB_20180813_X3_com.tif C:\Users\Emad\Desktop\cog\1\2\AEBB_20180813_X3_com.tif
C:\Users\Emad\Desktop\cog
['C:\\Users\\Emad\\Desktop\\cog\\AEBB_20180813_X3_com.tif', 'C:\\Users\\Emad\\Desktop\\cog\\1\\AEBB_20180813_X3_com.tif', 'C:\\Users\\Emad\\Desktop\\cog\\1\\2\\AEBB_20180813_X3_com.tif']

## Scripts

1. Creates a catalog of tiff files for conversion
2. Converts the images in the catalog, creating a mirrored folder structure in the destination
3. Chooses a random sample of images to validate

## Notes

The scripts have been designed to be compatible with Slurm compute clusters.

Example calls:
```
# Create Catalog
sbatch -p med -t 5 --job-name=NAIPcat ~/computing/clusterPy3.sh ~/cloud_optimization/1_create-catalog.py /share/spatial02/library/public/ca/imagery/imagery/naip/2016/ca_60cm_2016/

# Test conversion
sbatch -p med -t 20 --array=1 --job-name=2COG ~/computing/clusterPy3.sh ~/cloud_optimization/2_convert2cog.py /share/spatial02/library/public/ca/imagery/imagery/naip/2016/ca_60cm_2016/ /share/spatial03/library/public/ca/imagery/imagery/naip/2016/ca_60cm_2016/
```