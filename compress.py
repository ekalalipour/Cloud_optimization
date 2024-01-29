import sys

from osgeo import gdal
import subprocess

def get_max_overview(src_path, block_size=512):
	image = gdal.Open(src_path)
	width = image.RasterXSize
	height = image.RasterYSize
	nlevel = 0
	overview = 1
	while min(width // overview, height // overview) > block_size:
		overview *= 2
		nlevel += 1
	return nlevel

def check_overview(ds):
	main_band = ds.GetRasterBand(1)
	ovr_count = main_band.GetOverviewCount()
	if ovr_count == 0:
		return False
	else:
		return True

def create_cog(
	src_path,
	dst_path, 
	overview_resampling='nearest',
	overview_level=None,
	nodata=0,
	block_size=256,
	compress='RAW'):

	dataset = gdal.Open(src_path)

	out_profile = {
		'driver': 'GTiff',
		'tiled': 'YES',
		'block_size': 256,
		'copy_src_overviews': True, 
		'nodata': 0,
	}	

	if not overview_level:
		nlevel = get_max_overview(src_path)
	overview_list = [2 ** j for j in range(1, nlevel + 1)]
	overview_list = ' '.join([str(x) for x in overview_list])
    
	if not check_overview(dataset):
		overview_command = ' '.join(['gdaladdo', '--config COMPRESS={}'.format(compress), '-ro', '-r',\
			overview_resampling, src_path, overview_list ])
		print(overview_command)
		addo_result = subprocess.run(overview_command, shell=True, check=True)

	out_profile.update({'nodata':nodata, 'block_size':block_size})
	out_profile = dict(out_profile).values()
	translate_command = ' '.join(['gdal_translate', src_path, dst_path, '-co', 'TILED=YES'])
	print(translate_command)
	subprocess.run(translate_command, shell=True)

if __name__ == "__main__":
	src_path = 'C:\\Users\\Emad\\Documents\\sUAS\\AEBB_20180813_X3.tif'
	dest_path = 'C:\\Users\\Emad\\Documents\\sUAS\\compress.tif'

create_cog(src_path, dest_path, compress='jpeg')