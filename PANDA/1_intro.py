# print("Pnads allows us to analyze big data and make conclusions based on statistical theories.")

# print("Pandas can clean messy data sets, and make them readable ")

x='''A Series is essentially a column and Data frame is 2d arrray'''

data={
    'Apple':[3,2,0,1],
    'Orange':[0,3,7,2]
}

import pandas as pandav

purchases=pandav.DataFrame(data,index=['Harpal','Malay','Sahil','Jaylo'])

print(purchases)

fr_data={
    'Bhavnagar':['Dhar','Talaja','Dholka','Sihore'],

    'Botad':['Ranpur','Paliyad','Barvala','Botad'],

    'Amreli':['Lathi','Babra','Rajula','Liliya'],
   
}

dst=pandav.DataFrame(fr_data,index=['Sahil','Harpal','Jaylo','love'])

print(dst)

MahaBharat={
    'Ramayan':['Ram','Sita',['Laxman','Bharat','Satrughna'],'Ravan'],
    'Mahabharat':['Krishna','Radha',['Arjun','Bhim','Udhisthir','Nakul','Sahdev'],'Duryodhan'],
}

mb=pandav.DataFrame(MahaBharat,index=['Hero','Heroin','Helper','Villain'])

print(mb)
print('________\n')
mbf=mb.filter(like='Ram')

print(mbf)

print(pandav.__version__)

a = ['Harpal','Ram','Sita','Bharat','Satrughna']

myvar = pandav.Series(a)

print(myvar)
print(type(myvar))