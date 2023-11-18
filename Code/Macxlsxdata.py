# imports
import pandas as pd
import os
import numpy as np

# we can probably remove the below function if the automatic file reader works for both mac and windows. 



""" def readXLSXfilkes():
    #creating "master" dataframe for merging
    crimeDataDF = pd.DataFramecolumns=['CATEGORY','CALL GROUPS','final_case_type','CASE DESC', 'occ_date', 
                                    'x-coordinate', 'y_coordniate', 'census_tract']

    # Adding all sheet files (NOT geospatial files yet)
    # full years


    fullYear2013 = pd.read_excel(file_name+ r"/CIS635/Full Year/2013fullyear.xlsx")    fullYear2012 = pd.read_excel(file_name+ r"/CIS635/Full_Year/2012fullyear.xlsx")
    fullYear2014 = pd.read_excel(file_name+ r"/CIS635/2014/2014fullyear.xlsx")
    fullYear2015 = pd.read_excel(file_name+ r"/CIS635/Full Year/2015fullyear.xlsx")
    #2016
    janJuly2016 = pd.read_excel(file_name + r"/CIS635/2016/2016jan-july.xlsx")
    aug2016 = pd.read_excel(file_name+ r"/CIS635/2016/2016aug.xlsx")
    sept2016 = pd.read_excel(file_name+ r"/CIS635/2016/2016sept.xlsx")
    oct2016 = pd.read_excel(file_name+ r"/CIS635/2016/2016oct.xlsx")
    nov2016 = pd.read_excel(file_name+ r"/CIS635/2016/2016nov.xlsx")
    dec2016 = pd.read_excel(file_name+ r"/CIS635/2016/2016dec.xlsx")
    #2017
    jan2017 = pd.read_excel(file_name+ r"/CIS635/2017/2017jan.xlsx")
    feb_1_14_2017 = pd.read_excel(file_name+ r"/CIS635/2017/2017feb1-14.xlsx")
    feb_15_21_2017 = pd.read_excel(file_name+ r"/CIS635/2017/2017feb15-21.xlsx")
    feb_22_26_2017 = pd.read_excel(file_name+ r"/CIS635/2017/2017feb22-26.xlsx")
    feb_27_2017 = pd.read_excel(file_name+ r"/CIS635/2017/2017feb27.xlsx")
    feb_28_2017 = pd.read_excel(file_name + r"/CIS635/2017/2017feb28.xlsx")
    marMay2017 = pd.read_excel(file_name + r"/CIS635/2017/2017mar-may.xlsx")


    # removing fullYear2012, fullYear2013 because of intial merge
    dataList=[fullYear2014,fullYear2015, janJuly2016, aug2016, sept2016, 
            oct2016, nov2016, dec2016, jan2017, feb_1_14_2017, feb_15_21_2017, feb_22_26_2017, 
            feb_27_2017, feb_28_2017, marMay2017]

    #i'm sure there is a more elegent way to do this, 
    # but I am doing an intial merge, then doing a loop
    crimeDataDF = pd.merge(fullYear2012, fullYear2013, how = 'outer')
    for tempData in dataList:
        crimeDataDF = pd.merge(crimeDataDF, tempData, how = 'outer')

    return crimeDataDF """

 
# takes in a directory per machine (self-provided)
# defines our empty dataframe to populate with
# loops through the file path, and once we have an xlsx file, we take it and merge with our df
# returns our crime df
def fileReader(directory):
    crimeDataDF = pd.DataFrame(columns = ['CATEGORY','CALL GROUPS','final_case_type','CASE DESC', 'occ_date', 
                                    'x-coordinate', 'y_coordniate', 'census_tract'])

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.xlsx'):
                temp_file = pd.read_excel(dirpath + '/' + filename)
                crimeDataDF = crimeDataDF.merge(temp_file, how = 'outer')

    # code adds in two addtional nan-columns - deleting those
    crimeDataDF.drop(columns=crimeDataDF.columns[0:2], inplace=True)
    return crimeDataDF

# used to test a small version of our data so that we can ensure syntax/low level bugs are fixed before compliling actual dataset
def smallTesterFile(file_name = ""):
    fullYear2012 = pd.read_excel(file_name + r"/CIS635/Full Year/2012fullyear.xlsx")
    fullYear2013 = pd.read_excel(file_name + r"/CIS635/Full Year/2013fullyear.xlsx")
    testset = pd.merge(fullYear2012, fullYear2013, how = 'outer')
    return testset

# prints the nan's per column nicely
def nanColumns(df):
    new_df = df.copy()
    for column in new_df.columns:
        sum = new_df[column].isna().sum()
        print(column + " has " + str(sum) + " nans.")

        

# end of file
