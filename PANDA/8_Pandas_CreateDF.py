import pandas as pnd
a={
    'Name':['Harpal','Vishal','Purvi','Radha','Mahipat','Jay','Dhruvi','Vipul','Vanraj bhai','Payal','Payal'],
    'Relation':['Slef','Brother','Sister','Wife','Uncle','Nephew','Niece','Banevi','Mama','Bhabhi','Bhabhi'],
    'Location':['Rajkot','Ahmedabad','Rajkot','Rajkot','Jammu','Shirvaniya','Shirvaniya','Morbi','Surendranagar','Surendranagar','Devagadh']

}

df_detail = pnd.DataFrame(a,index=[19,17,18,19,26,5,1,33,43,23,24])
# print(df_detail)

# df_csv=df_detail.to_csv('Data_Details2.csv',index=False)

# print(df_detail.head(4))

# print(df_detail.tail(3))

# print(df_detail.describe())

mod_csv=pnd.read_csv('Data_Details2.csv')

# print(mod_csv)

mod_csv['Relation'][0]='Me'

# print(mod_csv)

mod_csv['Location'][2]='In My Heart'

print(mod_csv)
