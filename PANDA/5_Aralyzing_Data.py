import pandas as pnd

data_fram=pnd.read_csv('Z_Birthdata.csv')

print("Return 7 rows [Defaul 5]")
print(data_fram.head(7))

print("Return 6 rows [Defaul]")
print(data_fram.tail(6))

print("------------------------\n")

print(data_fram.info())