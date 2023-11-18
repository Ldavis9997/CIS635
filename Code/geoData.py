import geopandas as gpd
import matplotlib.pyplot as plt
import os
import pandas as pd
import fiona

def shpFileReader(directory):
    crimeData_geom = gpd.GeoDataFrame(columns=['CATEGORY', 'CALL_GROUP', 'final_case', 
                                               'CASE_DESC', 'occ_date', 'x_coordinate', 'y_coordinate', 
                                               'census_tract', 'geometry'], geometry='geometry')

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.shp'):
                with fiona.open(dirpath + '/' + filename) as shp:
                    temp_file = gpd.read_file(shp)
                    #temp_file = gpd.read_file(dirpath + '/' + filename, engine="pyogrio")
                    crimeData_geom = crimeData_geom.merge(temp_file, how = 'outer')

    return crimeData_geom


def shpFile_brute_MAC(fileName):

    #SHP_FEB27_2017 = gpd.read_file(fileName + r"/CIS635/Geo_Data/2017/NIJ2017_FEB27.shp")
    #SHP_FEB28_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB28.shp')
    #print(SHP_FEB28_2017)

    #2012
    SHP_MAR01_DEC31_2012 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2012/NIJ2012_MAR01_DEC31.shp')

    #2013
    SHP_JAN01_DEC31_2013 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2013/NIJ2013_JAN01_DEC31.shp')

    #2014
    SHP_JAN01_DEC31_2014 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2014/NIJ2014_JAN01_DEC31.shp')

    #2015
    SHP_JAN01_DEC31_2015 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2015/NIJ2015_JAN01_DEC31.shp')

    #2016 -JAN-JUL, AUG, SEP, OCT, NOV, DEC
    SHP_JAN01_JUL31_2016 = gpd.read_file(fileName + r'/IS635/Geo_Data/2016/NIJ2016_JAN01_JUL31.shp')

    SHP_AUG01_AUG31_2016 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2016/NIJ2016_AUG01_AUG31.shp')

    SHP_SEP01_SEP30_2016 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2016/NIJ2016_SEP01_SEP30.shp')

    SHP_OCT01_OCT31_2016 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2016/NIJ2016_OCT01_OCT31.shp')

    SHP_NOV01_NOV30_2016 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2016/NIJ2016_NOV01_NOV30.shp')

    SHP_DEC01_DEC31_2016 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2016/NIJ2016_DEC01_DEC31.shp')

    #2017 -JAN, FEB01-FEB14, FEB15-FEB21, FEB22-FEB26, FEB27, FEB28, MAR-MAY
    SHP_JAN01_JAN31_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_JAN01_JAN31.shp')

    SHP_FEB01_FEB14_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB01_FEB14.shp')

    SHP_FEB15_FEB21_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB15_FEB21.shp')

    SHP_FEB22_FEB26_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB22_FEB26.shp')

    SHP_FEB27_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB27.shp')

    SHP_FEB28_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_FEB28.shp')

    SHP_MAR01_MAY31_2017 = gpd.read_file(fileName + r'/CIS635/Geo_Data/2017/NIJ2017_MAR01_MAY31.shp')

    LIST_SHP_FILES = ['SHP_MAR01_DEC31_2012','SHP_JAN01_DEC31_2013','SHP_JAN01_DEC31_2014','SHP_JAN01_DEC31_2015','SHP_JAN01_JUL31_2016','SHP_AUG01_AUG31_2016','SHP_SEP01_SEP30_2016','SHP_OCT01_OCT31_2016','SHP_NOV01_NOV30_2016','SHP_DEC01_DEC31_2016','SHP_JAN01_JAN31_2017','SHP_FEB01_FEB14_2017','SHP_FEB15_FEB21_2017','SHP_FEB22_FEB26_2017','SHP_FEB27_2017','SHP_FEB28_2017','SHP_MAR01_MAY31_2017']

    print("hi")


def shpFile_brute_PC(directory = ""):
    #2012
    SHP_MAR01_DEC31_2012 = gpd.read_file(r'CIS635\Geo_Data\2012\NIJ2012_JAN01_DEC31.shp')

    #2013
    SHP_JAN01_DEC31_2013 = gpd.read_file(r'CIS635\Geo_Data\2013\NIJ2013_JAN01_DEC31.shp')

    #2014
    SHP_JAN01_DEC31_2014 = gpd.read_file(r'CIS635\Geo_Data\2014\NIJ2014_JAN01_DEC31.shp')

    #2015
    SHP_JAN01_DEC31_2015 = gpd.read_file(r'CIS635\Geo_Data\2015\NIJ2015_JAN01_DEC31.shp')

    #2016 -JAN-JUL, AUG, SEP, OCT, NOV, DEC
    SHP_JAN01_JUL31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_JAN01_JUL31.shp')

    SHP_AUG01_AUG31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_AUG01_AUG31.shp')

    SHP_SEP01_SEP30_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_SEP01_SEP30.shp')

    SHP_OCT01_OCT31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_OCT01_OCT31.shp')

    SHP_NOV01_NOV30_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_NOV01_NOV30.shp')

    SHP_DEC01_DEC31_2016 = gpd.read_file(r'CIS635\Geo_Data\2016\NIJ2016_DEC01_DEC31.shp')

    #2017 -JAN, FEB01-FEB14, FEB15-FEB21, FEB22-FEB26, FEB27, FEB28, MAR-MAY
    SHP_JAN01_JAN31_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_JAN01_JAN31.shp')

    SHP_FEB01_FEB14_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB01_FEB14.shp')

    SHP_FEB15_FEB21_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB15_FEB21.shp')

    SHP_FEB22_FEB26_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB22_FEB26.shp')

    SHP_FEB27_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB27.shp')

    SHP_FEB28_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_FEB28.shp')

    SHP_MAR01_MAY31_2017 = gpd.read_file(r'CIS635\Geo_Data\2017\NIJ2017_MAR01_MAY31.shp')

    LIST_SHP_FILES = ['SHP_MAR01_DEC31_2012','SHP_JAN01_DEC31_2013','SHP_JAN01_DEC31_2014','SHP_JAN01_DEC31_2015','SHP_JAN01_JUL31_2016','SHP_AUG01_AUG31_2016','SHP_SEP01_SEP30_2016','SHP_OCT01_OCT31_2016','SHP_NOV01_NOV30_2016','SHP_DEC01_DEC31_2016','SHP_JAN01_JAN31_2017','SHP_FEB01_FEB14_2017','SHP_FEB15_FEB21_2017','SHP_FEB22_FEB26_2017','SHP_FEB27_2017','SHP_FEB28_2017','SHP_MAR01_MAY31_2017']



# end of file
