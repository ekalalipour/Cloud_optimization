Created 2019
@author: Emad Kalalipour and Alex Mandel
Center for Spatial Sciences
University of California, Davis

TODO: Explain What Code Does

 source code:https://github.com/sshuair/cogeotiff/blob/master/cogeotiff/cog.py
             https://github.com/sshuair/cogeotiff/blob/master/cogeotiff/cog.py

 Osgeo command line > C:\\Users\\Emad\\Desktop\\CloudOptimize.py C:\Users\Emad\Desktop\test
 
 To generate COG > >gdal_translate 
 C:\\Users\\Emad\\Documents\\sUAS\\AEBB_20180813_X3.tif 
 C:\\Users\\Emad\\Documents\\sUAS\\input\\AEBB_20180813_X3_cog.tif -co TILED=YES -co /
 COPY_SRC_OVERVIEWS=YES -co COMPRESS=LZW

To validate the COG >> python3 C:\\Users\\Emad\\Documents\\sUAS\\validate_cloud_optimized_geotiff.py C:\\Users\\Emad\\Documents\\sUAS\\test.tif

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
"""
