import pandas as pd

ce='Computer Engineering'
student={
    'Enrollment_No':['21SOECE11013','21SOECE11014','21SOECE11054','21SOECE11040','21SOECE11159'],
    'First_Name':['Harpal','Gopi','Kuldip','Himanshu','Malay'],
    'Last_Name':['Dabhi','Dabhi','Mori','Kapuriya','Golatar'],
    'Branch':[ce,ce,ce,ce,ce],
    'City':['Botad','Patan','Surendranagar','Junagadh','Botad'],
    'Marks':[90,10,89,98,45]
}

student_df=pd.DataFrame(student)

student_df=pd.DataFrame(student,index=[1,2,3,4,5])

# student_df.to_csv('ClassList.csv')

filter_item=student_df.filter(items=['First_Name'])

# print(student_df)

# print(filter_item)

full_name=student_df['First_Name']+" "+student_df['Last_Name']

# print(full_name)

new_name=student_df.rename(columns={'First_Name':'FirstName', 'Last_Name':'LastName'})

# print(student_df)

# print('___________________')

# print(new_name)

updated=student_df['Marks']>80

print(updated)

passornot=student_df.loc[updated,'Marks']='Pass'

print(passornot)