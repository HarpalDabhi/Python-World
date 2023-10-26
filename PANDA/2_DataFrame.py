import pandas as pd
marks={
    'Harpal':[95,90,75],
    'Saahil':[35,50,60],
    'Jayraj':[35,36,34]
}

print(marks)

marsdf=pd.DataFrame(marks,index=['Gujarati','Hindi','Sanskrit'])

print(marsdf)

rnm=marsdf.rename(columns={'Harpal':'Malay'})

print(rnm)

students={
    'Boys':['harpal','vipul','adi','malay','jay'],
    'Girls':['Krishna','Karuna','Kirthy','Krupa','Kavita']
}

student_df=pd.DataFrame(students)

rnm1=student_df.rename(columns={'Boys':'Kumars','Girls':'Kanyas'})
# rnm2=student_df.rename(columns={'Girls':'Kanyas'})

print(student_df)

print('\n================================\n')

print(rnm1)

print(student_df.loc[2])

# print(rnm2)