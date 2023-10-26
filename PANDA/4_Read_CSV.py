import pandas as pandu

data_frame=pandu.read_csv('Z_Birthdata.csv')

print(data_frame.to_string())

print(data_frame)

print(pandu.options.display.max_rows)

print(data_frame.filter(like="Name"))