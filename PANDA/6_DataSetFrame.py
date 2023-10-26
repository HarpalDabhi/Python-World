import pandas as pd
a={
    'Name':['Harpal','Vipul','Malay','What'],
    'Dist':['Botad','Rajkot','Botad','Where'],
    'Age':[19,20,18,100]
}
# print(a)

a_df=pd.read_csv('Friends.csv')

print(a_df)
