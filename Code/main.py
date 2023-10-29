# imports
import pandas as pd

# had to put r before filepath to convert the string into a raw string, 
# I think because of the space between Full and Year
dataTest = pd.read_excel(r"CIS635\Full Year\2012fullyear.xlsx")
print(dataTest)

#testing again time number 3

