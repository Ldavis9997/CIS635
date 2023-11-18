# imports
import xlsxData
import Macxlsxdata as mac
import pandas as pd
import geoData 

#file_name = "/Users/lauryndavis/"
file_name = "/Users/Ldettling/Documents"

def mainRun(runType = 'Main', readGeo = False):
    if runType == 'Test':
        testdf = mac.smallTesterFile(file_name="/Users/Ldettling/Desktop")
        print(testdf)
        mac.nanColumns(testdf)
    else:
        crime_data = mac.fileReader(directory = "/Users/Ldettling/Documents/CIS635")
        print(crime_data)

        if readGeo:
            crimeData_geo = geoData.shpFile_brute_MAC(file_name)
            print(crimeData_geo)


mainRun()
