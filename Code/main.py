# imports
import xlsxData
import Macxlsxdata as mac
import pandas as pd
import geoData 

#file_name = "/Users/lauryndavis/"
file_name = "/Users/Ldettling/Documents"


# main file for running defs
#crimeDF = xlsxData.readXLSXfilkes()
#crimeDF = mac.readXLSXfilkes()
#print(crimeDF)

crime_data = mac.fileReader(directory = "/Users/Ldettling/Documents/CIS635")
print(crime_data)

#testdf = mac.smallTesterFile(file_name="/Users/Ldettling/Desktop")
#print(testdf)
#mac.nanColumns(testdf)

#crimeData_geo = 
#geoData.shpFile_brute_MAC(file_name)
#print(crimeData_geo)

# the above code is commented out for processing
