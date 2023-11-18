# imports
import xlsxData
import Macxlsxdata as mac
import pandas as pd
import geoData 

#file_name = "/Users/lauryndavis/"
file_name = "/Users/Ldettling/Documents"
data_directory = "/Users/Ldettling/Documents/CIS635"
geo_directory = "/Users/Ldettling/Documents/CIS635/Geo_Data"

def mainRun(runType = '', readGeo = False):
    if runType == 'Test':
        testdf = mac.smallTesterFile(file_name)
        print(testdf)
        mac.nanColumns(testdf)
    elif runType == 'Main':
        crime_data = mac.fileReader(data_directory)
        print(crime_data)

    if readGeo:
        crimeData_geo = geoData.shpFile_brute_MAC(file_name)
        #crimeData_geo = geoData.shpFileReader(geo_directory)
        print(crimeData_geo)

mainRun('Main', readGeo=False)
